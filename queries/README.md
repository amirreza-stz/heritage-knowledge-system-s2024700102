# SPARQL Queries

This directory contains SPARQL queries for querying the Heritage Knowledge System.

## Query Files

Queries are organized by functionality:

1. **`01_basic_queries.sparql`** - Basic queries for getting started
   - Count triples, list people, count items by type
   - Essential queries for verification and exploration

2. **`02_inference_queries.sparql`** - Inference testing queries
   - Test SpiritualGuardian inference
   - Compare explicit vs inferred types

3. **`03_validation_queries.sparql`** - Data validation queries
   - Find missing data (humanApproval, access levels)
   - Identify data quality issues
   - Check for violations

4. **`04_advanced_queries.sparql`** - Complex analysis queries
   - Statistical summaries
   - Relationship networks
   - Advanced reporting

## How to Use

   - Open GraphDB Workbench
   - Go to SPARQL tab
   - Copy and paste queries from these files
   - Click "Run" to execute