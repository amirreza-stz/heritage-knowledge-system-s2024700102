#!/usr/bin/env python3
"""
SHACL Validation Script
Runs SHACL validation on data files and saves reports

Usage:
    python code/run-shacl-validation.py <data.ttl> <shapes.shacl> <report.txt>
    
Example:
    python code/run-shacl-validation.py data/violations.ttl validation/temporal-constraints.shacl validation/validation-report-violations.txt
"""

import sys
from pathlib import Path

try:
    from pyshacl import validate
except ImportError:
    print("ERROR: pyshacl not installed!")
    print("Install it with: pip install pyshacl")
    sys.exit(1)


def run(data_path: str, shapes_path: str, out_path: str):
    """Run SHACL validation and save report"""
    data_path = Path(data_path)
    shapes_path = Path(shapes_path)
    out_path = Path(out_path)
    
    if not data_path.exists():
        print(f"ERROR: Data file not found: {data_path}")
        sys.exit(1)
    
    if not shapes_path.exists():
        print(f"ERROR: Shapes file not found: {shapes_path}")
        sys.exit(1)
    
    print(f"Loading data from: {data_path}")
    print(f"Loading shapes from: {shapes_path}")
    print(f"Running validation...")
    print("-" * 60)
    
    try:
        conforms, report_graph, report_text = validate(
            data_graph=str(data_path),
            shacl_graph=str(shapes_path),
            inference="rdfs",          # Use RDFS inference
            abort_on_first=False,
            allow_infos=True,
            allow_warnings=True,
            meta_shacl=False,
            advanced=True,
            debug=False,
        )
        
        # Save report
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report_text, encoding="utf-8")
        
        print()
        print("=" * 60)
        print("VALIDATION RESULTS")
        print("=" * 60)
        print(f"Conforms: {'YES ✓' if conforms else 'NO ✗'}")
        print(f"Report saved to: {out_path}")
        print()
        
        if not conforms:
            # Count violations
            from rdflib.namespace import SH
            violations = list(report_graph.subjects(
                predicate=None,
                object=SH.ValidationResult
            ))
            print(f"Total violations found: {len(violations)}")
            print()
            print("First 10 lines of report:")
            print("-" * 60)
            lines = report_text.split('\n')[:10]
            for line in lines:
                print(line)
        else:
            print("No violations found! ✓")
        
        return conforms
        
    except Exception as e:
        print(f"ERROR during validation: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python code/run-shacl-validation.py <data.ttl> <shapes.shacl> <report.txt>")
        print()
        print("Examples:")
        print("  python code/run-shacl-validation.py data/violations.ttl validation/temporal-constraints.shacl validation/validation-report-violations.txt")
        print("  python code/run-shacl-validation.py data/fixed-data.ttl validation/temporal-constraints.shacl validation/validation-report-clean.txt")
        sys.exit(2)
    
    run(sys.argv[1], sys.argv[2], sys.argv[3])
