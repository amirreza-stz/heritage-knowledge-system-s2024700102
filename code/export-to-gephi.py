#!/usr/bin/env python3
"""
Export RDF data to GEXF format for Gephi visualization.

This script converts the heritage knowledge base to a graph format
that can be imported into Gephi for network visualization.
"""

import sys
from rdflib import Graph, Namespace, RDF, RDFS, URIRef
from rdflib.namespace import XSD
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Namespace
NS = Namespace("http://www.semanticweb.org/ubuntu/ontologies/2026/0/s2024700102heritage/")

def get_label(graph, uri):
    """Get English label for a URI, or use the local name."""
    labels = list(graph.objects(uri, RDFS.label))
    for label in labels:
        if hasattr(label, 'language') and (label.language == 'en' or label.language == ''):
            return str(label)
    # Fallback to local name
    return str(uri).split('#')[-1].split('/')[-1]

def get_type(graph, uri):
    """Get the type(s) of an entity."""
    types = []
    for obj in graph.objects(uri, RDF.type):
        if str(obj).startswith(str(NS)):
            types.append(str(obj).split('/')[-1])
    return types

def get_access_level(graph, uri):
    """Get access level if it's a Person."""
    access = list(graph.objects(uri, NS.hasAccessLevel))
    if access:
        return int(access[0])
    return None

def is_elder(graph, uri):
    """Check if entity is a TribalElder."""
    return (uri, RDF.type, NS.TribalElder) in graph

def export_to_gexf(data_file, output_file, include_properties=None):
    """
    Export RDF data to GEXF format.
    
    Args:
        data_file: Path to RDF data file (TTL format)
        output_file: Path to output GEXF file
        include_properties: List of property URIs to include as edges (None = all object properties)
    """
    print(f"Loading RDF data from: {data_file}")
    g = Graph()
    g.parse(data_file, format="turtle")
    print(f"Loaded {len(g)} triples")
    
    # Collect all nodes and edges
    nodes = {}
    edges = []
    node_id_map = {}
    next_id = 0
    
    # Object properties to include (relationships)
    object_properties = [
        NS.hasRole,
        NS.memberOfCommunity,
        NS.playsInstrument,
        NS.knowsMusicalWork,
        NS.knowsStory,
        NS.performedInRitual,
        NS.caresFor,
        NS.hasCompetency,
        NS.mentoredBy,
        NS.approvedBy,
        NS.performedBy,
        NS.usesInstrument,
        NS.recordedAt,
        NS.locatedIn,
    ]
    
    # Collect all entities (nodes)
    print("Collecting nodes...")
    all_subjects = set(g.subjects())
    all_objects = set()
    
    for prop in object_properties:
        for obj in g.objects(None, prop):
            if isinstance(obj, URIRef) and str(obj).startswith(str(NS)):
                all_objects.add(obj)
    
    all_nodes = all_subjects | all_objects
    
    for uri in all_nodes:
        if str(uri).startswith(str(NS)):
            node_id = f"n{next_id}"
            node_id_map[uri] = node_id
            next_id += 1
            
            label = get_label(g, uri)
            types = get_type(g, uri)
            node_type = types[0] if types else "Entity"
            
            node_data = {
                'id': node_id,
                'label': label,
                'uri': str(uri),
                'type': node_type,
                'types': types,
            }
            
            # Add Person-specific attributes
            if NS.Person in types or NS.TribalElder in types:
                access_level = get_access_level(g, uri)
                if access_level is not None:
                    node_data['access_level'] = access_level
                if is_elder(g, uri):
                    node_data['is_elder'] = True
            
            nodes[uri] = node_data
    
    print(f"Found {len(nodes)} nodes")
    
    # Collect edges (relationships)
    print("Collecting edges...")
    for prop in object_properties:
        prop_name = str(prop).split('/')[-1]
        for s, o in g.subject_objects(prop):
            if s in node_id_map and o in node_id_map:
                edges.append({
                    'source': node_id_map[s],
                    'target': node_id_map[o],
                    'type': prop_name,
                    'label': prop_name
                })
    
    print(f"Found {len(edges)} edges")
    
    # Create GEXF XML
    print("Creating GEXF file...")
    gexf = ET.Element('gexf')
    gexf.set('xmlns', 'http://www.gexf.net/1.3')
    gexf.set('version', '1.3')
    gexf.set('xmlns:viz', 'http://www.gexf.net/1.3/viz')
    
    meta = ET.SubElement(gexf, 'meta')
    meta.set('lastmodifieddate', '2026-01-19')
    creator = ET.SubElement(meta, 'creator')
    creator.text = 'Heritage Knowledge System Export'
    description = ET.SubElement(meta, 'description')
    description.text = 'Cultural Heritage Knowledge Base Network'
    
    graph = ET.SubElement(gexf, 'graph')
    graph.set('mode', 'static')
    graph.set('defaultedgetype', 'directed')
    
    # Attributes
    attributes = ET.SubElement(graph, 'attributes')
    attributes.set('class', 'node')
    
    attr_type = ET.SubElement(attributes, 'attribute')
    attr_type.set('id', 'type')
    attr_type.set('title', 'Type')
    attr_type.set('type', 'string')
    
    attr_access = ET.SubElement(attributes, 'attribute')
    attr_access.set('id', 'access_level')
    attr_access.set('title', 'Access Level')
    attr_access.set('type', 'integer')
    
    # Nodes
    nodes_elem = ET.SubElement(graph, 'nodes')
    for uri, node_data in nodes.items():
        node = ET.SubElement(nodes_elem, 'node')
        node.set('id', node_data['id'])
        node.set('label', node_data['label'])
        
        # Attributes
        attvalues = ET.SubElement(node, 'attvalues')
        
        attvalue_type = ET.SubElement(attvalues, 'attvalue')
        attvalue_type.set('for', 'type')
        attvalue_type.set('value', node_data['type'])
        
        if 'access_level' in node_data:
            attvalue_access = ET.SubElement(attvalues, 'attvalue')
            attvalue_access.set('for', 'access_level')
            attvalue_access.set('value', str(node_data['access_level']))
        
        # Visualization attributes (size based on type)
        viz_size = ET.SubElement(node, '{http://www.gexf.net/1.3/viz}size')
        if node_data['type'] == 'Person':
            viz_size.set('value', '15')
        elif node_data['type'] == 'TribalElder':
            viz_size.set('value', '20')
        elif node_data['type'] == 'Location':
            viz_size.set('value', '12')
        elif node_data['type'] == 'Community':
            viz_size.set('value', '14')
        else:
            viz_size.set('value', '10')
        
        # Color based on type
        viz_color = ET.SubElement(node, '{http://www.gexf.net/1.3/viz}color')
        if node_data['type'] == 'Person' or node_data['type'] == 'TribalElder':
            viz_color.set('r', '100')
            viz_color.set('g', '150')
            viz_color.set('b', '200')
        elif node_data['type'] == 'Location':
            viz_color.set('r', '200')
            viz_color.set('g', '100')
            viz_color.set('b', '100')
        elif node_data['type'] == 'Community':
            viz_color.set('r', '150')
            viz_color.set('g', '200')
            viz_color.set('b', '100')
        elif node_data['type'] == 'Instrument' or 'Instrument' in node_data['types']:
            viz_color.set('r', '200')
            viz_color.set('g', '200')
            viz_color.set('b', '100')
        else:
            viz_color.set('r', '180')
            viz_color.set('g', '180')
            viz_color.set('b', '180')
    
    # Edges
    edges_elem = ET.SubElement(graph, 'edges')
    for i, edge in enumerate(edges):
        edge_elem = ET.SubElement(edges_elem, 'edge')
        edge_elem.set('id', f"e{i}")
        edge_elem.set('source', edge['source'])
        edge_elem.set('target', edge['target'])
        edge_elem.set('label', edge['label'])
        edge_elem.set('weight', '1.0')
    
    # Write to file
    xml_str = minidom.parseString(ET.tostring(gexf)).toprettyxml(indent="  ")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(xml_str)
    
    print(f"\n✓ GEXF file created: {output_file}")
    print(f"  Nodes: {len(nodes)}")
    print(f"  Edges: {len(edges)}")
    print(f"\nImport this file into Gephi to visualize the network!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python code/export-to-gephi.py <data_file> [output_file]")
        print("Example: python code/export-to-gephi.py data/heritage_base_dataset.ttl visualizations/heritage_network.gexf")
        sys.exit(1)
    
    data_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "visualizations/heritage_network.gexf"
    
    try:
        export_to_gexf(data_file, output_file)
    except ImportError as e:
        print(f"Error: Missing required library. Install with: pip install rdflib")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
