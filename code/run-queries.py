#!/usr/bin/env python3
"""
SPARQL Query Execution Script
Runs SPARQL queries against a Fuseki endpoint and saves results as JSON

Usage:
    python code/run-queries.py <endpoint_url>
    
Example:
    python code/run-queries.py http://localhost:3030/heritage-reification/sparql
"""

import json
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: requests library not installed!")
    print("Install it with: pip install requests")
    sys.exit(1)


def run_query(endpoint: str, rq_file: Path):
    """Execute a SPARQL query against an endpoint"""
    query = rq_file.read_text(encoding="utf-8")
    
    print(f"Executing: {rq_file.name}")
    
    try:
        response = requests.post(
            endpoint,
            data={"query": query},
            headers={"Accept": "application/sparql-results+json"},
            timeout=60,
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"ERROR executing query {rq_file.name}: {e}")
        return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python code/run-queries.py <endpoint_url>")
        print()
        print("Examples:")
        print("  python code/run-queries.py http://localhost:3030/heritage-reification/sparql")
        print("  python code/run-queries.py http://localhost:3030/heritage-named/sparql")
        print("  python code/run-queries.py http://localhost:3030/heritage-rdfstar/sparql")
        sys.exit(2)
    
    endpoint = sys.argv[1]
    queries_dir = Path("queries")
    out_dir = queries_dir / "results"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    if not queries_dir.exists():
        print(f"ERROR: Queries directory not found: {queries_dir}")
        sys.exit(1)
    
    print(f"Query endpoint: {endpoint}")
    print(f"Queries directory: {queries_dir}")
    print(f"Results directory: {out_dir}")
    print("-" * 60)
    
    # Find all .rq files
    query_files = sorted(queries_dir.glob("*.rq"))
    
    if not query_files:
        print("No .rq files found in queries directory")
        sys.exit(1)
    
    for rq_file in query_files:
        result = run_query(endpoint, rq_file)
        
        if result:
            out_path = out_dir / (rq_file.stem + ".json")
            out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
            print(f"  ✓ Saved: {out_path}")
            
            # Show result count
            if "results" in result and "bindings" in result["results"]:
                count = len(result["results"]["bindings"])
                print(f"    Results: {count} rows")
        else:
            print(f"  ✗ Failed: {rq_file.name}")
        print()
    
    print("=" * 60)
    print("Query execution complete!")
    print(f"Results saved to: {out_dir}")
