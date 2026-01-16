#!/usr/bin/env python3
"""
SHACL Validation Test Script
Tests data against validation shapes
"""

import sys

try:
    import pyshacl
    from rdflib import Graph
except ImportError:
    print("ERROR: pyshacl not installed!")
    print("Install it with: pip install pyshacl")
    sys.exit(1)

def main():
    print("=" * 60)
    print("SHACL Validation Test")
    print("=" * 60)
    print()
    
    # Load shapes
    print("Loading SHACL shapes...")
    shapes_graph = Graph()
    try:
        shapes_graph.parse("shapes/validation_shapes.ttl", format="turtle")
        print(f"✓ Loaded {len(shapes_graph)} triples from validation shapes")
    except Exception as e:
        print(f"✗ Error loading shapes: {e}")
        sys.exit(1)
    
    # Load data
    print("Loading data...")
    data_graph = Graph()
    try:
        data_graph.parse("data/heritage_base_dataset.ttl", format="turtle")
        print(f"✓ Loaded {len(data_graph)} triples from data")
    except Exception as e:
        print(f"✗ Error loading data: {e}")
        sys.exit(1)
    
    print()
    print("Running SHACL validation...")
    print("-" * 60)
    
    # Run validation
    try:
        conforms, results_graph, results_text = pyshacl.validate(
            data_graph,
            shacl_graph=shapes_graph,
            inference='rdfs',
            abort_on_first=False,
            allow_infos=False,
            allow_warnings=False,
            meta_shacl=False,
            advanced=False,
            js=False,
            debug=False
        )
        
        print()
        print("=" * 60)
        print("VALIDATION RESULTS")
        print("=" * 60)
        print(f"Conforms: {'✓ YES' if conforms else '✗ NO'}")
        print()
        
        if not conforms:
            # Count violations
            from rdflib.namespace import SH
            violations = list(results_graph.subjects(
                predicate=None,
                object=SH.ValidationResult
            ))
            print(f"Total violations found: {len(violations)}")
            print("Expected: 4 violations (by design, for testing)")
            print()
            print("Detailed Report:")
            print("-" * 60)
            print(results_text)
        else:
            print("No violations found!")
            print("(Note: Your data is designed to have 4 violations)")
        
        # Save report
        if results_graph:
            results_graph.serialize("validation_report.ttl", format="turtle")
            print()
            print(f"✓ Detailed report saved to: validation_report.ttl")
        
    except Exception as e:
        print(f"✗ Error during validation: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
