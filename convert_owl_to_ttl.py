#!/usr/bin/env python3
"""
Script to convert OWL ontology file to TTL (Turtle) format.
This script uses rdflib to parse the OWL file and serialize it as Turtle.
"""

from rdflib import Graph
import sys
import os

def convert_owl_to_ttl(owl_file_path, ttl_file_path=None):
    """
    Convert an OWL file to TTL format.
    
    Args:
        owl_file_path: Path to the input OWL file
        ttl_file_path: Path to the output TTL file (optional, defaults to same name with .ttl extension)
    """
    if not os.path.exists(owl_file_path):
        print(f"Error: File not found: {owl_file_path}")
        sys.exit(1)
    
    if ttl_file_path is None:
        base_name = os.path.splitext(owl_file_path)[0]
        ttl_file_path = f"{base_name}.ttl"
    
    print(f"Loading OWL file: {owl_file_path}")
    g = Graph()
    
    try:
        # Parse the OWL file
        g.parse(owl_file_path, format="xml")
        print(f"Successfully parsed OWL file. Found {len(g)} triples.")
        
        # Serialize to Turtle format
        print(f"Converting to TTL format: {ttl_file_path}")
        g.serialize(destination=ttl_file_path, format="turtle")
        print(f"Successfully converted to TTL format!")
        print(f"Output file: {ttl_file_path}")
        
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_owl_to_ttl.py <owl_file> [ttl_file]")
        print("Example: python convert_owl_to_ttl.py ontology/my_ontology.owl")
        sys.exit(1)
    
    owl_file = sys.argv[1]
    ttl_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_owl_to_ttl(owl_file, ttl_file)
