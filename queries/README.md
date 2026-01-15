# SPARQL Queries

This directory contains SPARQL queries for querying the Heritage Knowledge System.

## Query Files

Queries will be organized by functionality:
- `access_control_queries.sparql` - Queries related to access levels and permissions
- `cultural_items_queries.sparql` - Queries about artifacts, rituals, and cultural items
- `people_queries.sparql` - Queries about people, roles, and relationships
- `location_queries.sparql` - Queries about locations and geographical data
- `approval_queries.sparql` - Queries about approval workflows

## Example Query Structure

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX wp: <http://webprotege.stanford.edu/>
PREFIX ex: <http://example.org/heritage#>

# Query description here
SELECT ?subject ?predicate ?object
WHERE {
    # Query pattern here
}
```
