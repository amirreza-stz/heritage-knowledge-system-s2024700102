#!/usr/bin/env python3
"""
Triplestore Loading Helper Script
Provides instructions for loading data into Fuseki or GraphDB

Note: The easiest way is to use the Fuseki/GraphDB web UI and take screenshots.
This script provides a programmatic alternative using Fuseki's HTTP API.
"""

import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: requests library not installed!")
    print("Install it with: pip install requests")
    sys.exit(1)


def load_to_fuseki(dataset_name: str, file_path: Path, fuseki_url: str = "http://localhost:3030"):
    """Load a TTL file into a Fuseki dataset"""
    upload_url = f"{fuseki_url}/{dataset_name}/data"
    
    print(f"Loading {file_path.name} into dataset: {dataset_name}")
    print(f"Upload URL: {upload_url}")
    
    try:
        with open(file_path, 'rb') as f:
            files = {'file': (file_path.name, f, 'text/turtle')}
            response = requests.post(upload_url, files=files, timeout=60)
            response.raise_for_status()
            print(f"✓ Successfully loaded {file_path.name}")
            return True
    except requests.exceptions.RequestException as e:
        print(f"✗ Error loading file: {e}")
        print()
        print("Alternative: Use Fuseki web UI:")
        print(f"  1. Open http://localhost:3030")
        print(f"  2. Select dataset: {dataset_name}")
        print(f"  3. Click 'Upload files'")
        print(f"  4. Select: {file_path}")
        print(f"  5. Take screenshot of successful upload")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("Triplestore Loading Helper")
    print("=" * 60)
    print()
    print("RECOMMENDED: Use Fuseki/GraphDB web UI for loading data")
    print("This provides visual confirmation and screenshots for submission.")
    print()
    print("Fuseki Web UI:")
    print("  1. Start Fuseki: ./fuseki-server")
    print("  2. Open: http://localhost:3030")
    print("  3. Create datasets: heritage-reification, heritage-named, heritage-rdfstar")
    print("  4. Upload files through web interface")
    print("  5. Take screenshots of successful data loading")
    print()
    print("GraphDB Web UI:")
    print("  1. Start GraphDB: ./bin/graphdb")
    print("  2. Open: http://localhost:7200")
    print("  3. Create repositories")
    print("  4. Import files through web interface")
    print("  5. Take screenshots of successful data loading")
    print()
    print("=" * 60)
    print()
    
    if len(sys.argv) >= 3:
        dataset_name = sys.argv[1]
        file_path = Path(sys.argv[2])
        fuseki_url = sys.argv[3] if len(sys.argv) > 3 else "http://localhost:3030"
        
        if not file_path.exists():
            print(f"ERROR: File not found: {file_path}")
            sys.exit(1)
        
        load_to_fuseki(dataset_name, file_path, fuseki_url)
    else:
        print("For programmatic loading (optional):")
        print("  python code/load-triplestore.py <dataset_name> <file.ttl> [fuseki_url]")
        print()
        print("Example:")
        print("  python code/load-triplestore.py heritage-reification data/contested-claims-reification.ttl")
