# Heritage Knowledge System - Final Project

This repository contains the implementation for the final project of the Social Semantic Web course taught by Prof. Dr. Suzan Üsküdarlı at Boğaziçi University CMPE.

## Project Overview

The Heritage Knowledge System is an ontology-based system designed to model and manage cultural heritage information, including artifacts, rituals, locations, people, and their relationships. The system supports access control, approval workflows, and cultural preservation documentation.

## Learner Information

- **Name**: Amirreza Sattarzadeh KhanehBargh 
- **Student ID**: 2024700102

## Limitations and Challenges

**macOS Compatibility**
   - GraphDB, Fuseki, and Protégé have compatibility issues on macOS
   - Tried to use alternative device or virtual machine


**Date Format**
   - Uses `xsd:date` for recording dates
   - Could be extended to `xsd:dateTime` for more precision

**Approval Process**
   - Binary approval (true/false)
   - Could be extended with approval levels or workflow states

**Tool Compatibility**
   - macOS issues with semantic web tools
   - Required workaround approach

**My hard illness and Iran connection block : I can not connect to my family and friends and this harms my focus and thinking power**

## Project Structure

```
heritage-knowledge-system-s2024700102/
├── ontology/
│   ├── urn_webprotege_ontology_f1486f8e-61de-449c-a0d0-d0b65f032faf.owl  # Original OWL ontology
│   └── heritage_ontology.ttl                                             # Converted TTL ontology (138 triples)
├── data/
│   ├── heritage_base_dataset.ttl                                         # Main dataset: 30 people + 50 items (277 triples)
│   └── example_data.ttl                                                  # Example instance data (79 triples)
├── queries/
│   └── (SPARQL queries will be placed here)
├── convert_owl_to_ttl.py                                                 # Conversion script
├── requirements.txt                                                       # Python dependencies
└── README.md                                                              # This file
```

## Tools and Versions

- **Protégé**: WebProtégé (used for ontology development)
  - Note: Desktop Protégé had compatibility issues on macOS; will be tested on alternative device
- **Triplestore**: GraphDB Free 11.2.0 (planned)
  - Note: Installation completed but testing deferred due to macOS compatibility issues
  - Alternative: Apache Jena Fuseki on a windows or ubuntu device
- **Programming Language**: Python3
- **Libraries**:
  - `rdflib >= 6.0.0` - RDF parsing and manipulation
  - `pyshacl >= 0.20.0` - SHACL validation (optional)

## Ontology Overview

### Main Classes

- **CulturalEntity** (root class)
  - **Person**: Represents individuals in the system
    - Performer
    - TribalElder
    - Archaeologist
    - Guardian
  - **CulturalItem**: Represents cultural artifacts and practices
    - Artifact
    - SacredItem
    - Ritual
    - Instrument
    - ArchaeologicalSite
  - **Role**: Represents roles that people can have
    - Guardian
    - Researcher
    - SpiritualGuardian
  - **Location**: Represents geographical locations
    - Region
    - Site
  - **AccessLevel**: Represents access control levels
    - Public
    - Restricted
    - Sacred

### Object Properties

- `recordedAt`: Links cultural items to locations
- `approvedBy`: Links items to tribal elders who approved them
- `playsInstrument`: Links performers to instruments
- `isCaredBy`: Links cultural items to people who care for them
- `hasRole`: Links people to their roles
- `aboutItem`: Links items to related items
- `caresFor`: Inverse of isCaredBy
- `hasAccessLevel`: Links people to their access levels
- `isRoleOf`: Inverse of hasRole
- `performs`: Links performers to rituals
- `hasRequiredAccessLevel`: Links cultural items to required access levels
- `locatedIn`: Links locations to parent locations

### Data Properties

- `recordingDate`: Date when a cultural item was recorded (xsd:date)
- `humanApproval`: Boolean indicating human approval status (xsd:boolean)

## Setup Instructions

### Prerequisites

1. Python 3.7 or higher
2. pip (Python package manager)

### Installation

1. Clone or download this repository

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

### Converting OWL to TTL

To convert the OWL ontology file to TTL format:

```bash
python convert_owl_to_ttl.py ontology/urn_webprotege_ontology_f1486f8e-61de-449c-a0d0-d0b65f032faf.owl
```

Or specify an output file:

```bash
python convert_owl_to_ttl.py ontology/urn_webprotege_ontology_f1486f8e-61de-449c-a0d0-d0b65f032faf.owl ontology/heritage_ontology.ttl
```

## Usage

### Loading the Ontology

The ontology is available in both OWL and TTL formats:
- **OWL**: `ontology/urn_webprotege_ontology_f1486f8e-61de-449c-a0d0-d0b65f032faf.owl`
- **TTL**: `ontology/heritage_ontology.ttl`

### Example Data

Two data files are provided:

1. **`data/heritage_base_dataset.ttl`** - Main dataset for the project:
   - **30 people** (2 elders, 5 guardians, 5 performers, 2 archaeologists, 16 general persons)
   - **50 cultural items** (10 sacred items, 10 rituals, 10 instruments, 10 artifacts, 10 archaeological sites)
   - Designed to enable inference of ≥5 SpiritualGuardians (once equivalent-class axiom is added in Protégé)
   - Includes human-approval violations for SHACL testing
   - Uses student ID prefix: `http://example.org/heritage/s2024700102#`
   - Total: 277 triples

2. **`data/example_data.ttl`** - Smaller example dataset for testing:
   - Demonstrates basic relationships and structure
   - Useful for initial testing and understanding the ontology

## Next Steps

### Completed ✅
- Ontology conversion (OWL → TTL)
- Data files created and verified
- SPARQL queries created (35+ queries)
- SHACL validation shapes created
- Documentation structure in place

### To Complete on Alternative Device ⏳
- Add equivalent-class axiom in Protégé
- Test queries in triplestore (GraphDB/Fuseki)
- Verify inference results
- Run SHACL validation
- Capture query results and screenshots

## Brief Answer for Analysis Questions

TBD :
- Ontology design decisions and rationale
- Data structure analysis
- Query design and expected results
- Relationship modeling approach

### Key Design Decisions

1. **Hierarchical Class Structure**: Root `CulturalEntity` class provides common base for all entities, enabling flexible relationship modeling.

2. **Access Control Model**: Three-tier system (Public, Restricted, Sacred) applied to both people and cultural items, supporting fine-grained access control.

3. **Role-Based System**: Roles as separate entities allow people to have multiple roles and enable inference of specialized roles (e.g., SpiritualGuardian).

4. **Approval Workflow**: Links to TribalElder and tracks approval status, supporting cultural sensitivity requirements.

## Limits and Challenges

### Technical Challenges

1. **macOS Compatibility**: GraphDB, Fuseki, and Protégé desktop had compatibility issues on macOS. Workaround: Testing deferred to alternative device.

2. **WebProtégé URIs**: Non-human-readable URIs make queries verbose. Mitigated with proper prefix usage and documentation.

3. **Inference Testing**: Requires equivalent-class axiom in Protégé and triplestore for testing. Axiom definition prepared but testing deferred.

### Design Limitations

1. **Date Precision**: Uses `xsd:date`; could be extended to `xsd:dateTime` for more precision.

2. **Access Control**: Simple three-tier system; could be extended with more granular permissions.

3. **Approval Process**: Binary approval; could be extended with approval levels or workflow states.

### Future Improvements

1. Enhanced inference with more equivalent-class axioms
2. Extended SHACL validation with comprehensive shapes
3. Query optimization and indexing
4. Visualization of ontology structure

## License

This project is part of an academic course assignment.
