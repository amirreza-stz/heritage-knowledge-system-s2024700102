# Heritage Knowledge System - Final Project

This repository contains the implementation for the final project of the Social Semantic Web course taught by Prof. Dr. Suzan Üsküdarlı at Boğaziçi University CMPE.


###  *** I had some variuos challenges during implementation of this project (Such as my hard illness, my migration to MacOS and compatibility problems with this OS, and the problems and challenges related to my mental health and connection bloch with my family and country and etc) but I tried to completely understand and answer all of the requirements of the project, using more time and also with the help of AI assistants (but I used them just as assistant and not a team-mate, and understood every part or help that I used them). 

*** Also because of my challenges with MacOS, I will use an alternative Laptop from a friend to test and run protege, fuseki/graphDB.


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
│   └── heritage-s2024700102.ttl                                          # Updated TTL ontology with equivalent-class axiom (286 triples)
├── data/
│   ├── heritage_base_dataset.ttl                                         # Main dataset: 30 people + 50 items (277 triples)
│   └── example_data.ttl                                                  # Example instance data (79 triples)
├── queries/
│   ├── 00_verification_queries.sparql                                    # Verification queries
│   ├── 01_basic_queries.sparql                                           # Basic exploration queries
│   ├── 02_inference_queries.sparql                                       # Inference testing queries
│   ├── 03_validation_queries.sparql                                     # Data quality queries
│   └── 04_advanced_queries.sparql                                       # Advanced analysis queries
├── shapes/
│   └── validation_shapes.ttl                                             # SHACL validation shapes
├── convert_owl_to_ttl.py                                                 # Conversion script
├── requirements.txt                                                       # Python dependencies
└── README.md                                                              # This file
```

## Tools and Versions

### Ontology Development
- **Protégé**: Desktop Protégé (tested on Ubuntu)
  - Used for: Ontology editing, adding equivalent-class axiom, inference testing
  - Reasoner: HermiT 
  - Note: Desktop Protégé had compatibility issues on macOS; tested on Ubuntu alternative device

### Triplestore
- **Apache Jena Fuseki**: Latest version (tested on Ubuntu)
  - Used for: SPARQL query testing, data loading

### Programming Language
- **Python 3**
  - Used for: OWL to TTL conversion, SHACL validation, data verification

### Python Libraries
- **rdflib**: >= 6.0.0
  - Purpose: RDF parsing, manipulation, and serialization
  - Used in: `convert_owl_to_ttl.py`, data verification scripts
- **pyshacl**: >= 0.20.0
  - Purpose: SHACL validation
  - Used in: `test_shacl.py` for validating data against SHACL shapes

### Standards and Formats
- **OWL**: 2.0 (Web Ontology Language)
- **RDF**: RDF 1.1 (Resource Description Framework)
- **SPARQL**: SPARQL 1.1 (Query language)
- **SHACL**: SHACL 1.1 (Shapes Constraint Language)
- **Turtle**: TTL syntax for RDF serialization

### Testing and Validation
- **SHACL Validation**: Using pySHACL library
  - Script: `test_shacl.py` (included in repository)
  - Shapes: `shapes/validation_shapes.ttl` (8 validation shapes)
  - Expected: 4 violations (by design, for testing)

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

1. **Python 3.7 or higher**
2. **pip**: Python package manager
3. **Protégé**: Desktop version (for ontology editing and inference testing)
   - Download: https://protege.stanford.edu/
   - Alternative: WebProtégé (browser-based)
4. **Triplestore** (choose one):
   - **Apache Jena Fuseki**: For SPARQL query testing
     - Download: https://jena.apache.org/download/
### Installation

1. **Clone or download this repository**

2. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

This will install:
- `rdflib >= 6.0.0` - For RDF processing
- `pyshacl >= 0.20.0` - For SHACL validation

3. **Install Protégé** (for ontology editing):
   - Download from: https://protege.stanford.edu/
   - Extract and run (Java required)

4. **Install Triplestore** (choose one):
   - **Fuseki**: Download from https://jena.apache.org/download/

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
- **OWL**: `ontology/urn_webprotege_ontology_f1486f8e-61de-449c-a0d0-d0b65f032faf.owl` (original)
- **TTL**: `ontology/heritage-s2024700102.ttl` (updated with equivalent-class axiom for SpiritualGuardian inference)

### Example Data

Two data files are provided:

1. **`data/heritage_base_dataset.ttl`** - Main dataset for the project:
   - **30 people** (2 elders, 5 guardians, 5 performers, 2 archaeologists, 16 general persons)
   - **50 cultural items** (10 sacred items, 10 rituals, 10 instruments, 10 artifacts, 10 archaeological sites)
   - Designed to enable inference of ≥5 SpiritualGuardians (equivalent-class axiom added in `heritage-s2024700102.ttl`)
   - Includes human-approval violations for SHACL testing
   - Uses student ID prefix: `http://example.org/heritage/s2024700102#`
   - Total: 277 triples

2. **`data/example_data.ttl`** - Smaller example dataset for testing:
   - Demonstrates basic relationships and structure
   - Useful for initial testing and understanding the ontology

### Running SHACL Validation

To validate your data against SHACL shapes:

```bash
# Install pySHACL if not already installed
pip install pyshacl

# Run validation
python3 test_shacl.py
```

This will:
- Load SHACL shapes from `shapes/validation_shapes.ttl` (8 validation shapes)
- Validate data from `data/heritage_base_dataset.ttl`
- Report violations 
- Save detailed report to `validation_report.ttl`

## Next Steps

### Completed ✅
- Ontology conversion (OWL → TTL)
- Ontology updated with equivalent-class axiom for SpiritualGuardian inference
- Data files created and verified
- SPARQL queries created (43 queries across 5 files)
- SHACL validation shapes created
- Documentation structure in place

### Testing Status ⏳
- ✅ Protégé: Equivalent-class axiom added and tested
- ✅ Fuseki: Data loaded and queries tested
- ⏳ Inference: Verify 5 SpiritualGuardians inferred in triplestore
- ⏳ SHACL Validation: Run `test_shacl.py` to validate data
- ⏳ Documentation: Capture query results and screenshots

## Brief Answer for Analysis Questions

See `ANALYSIS_AND_DOCUMENTATION.md` for comprehensive analysis. Summary below:

### Key Design Decisions

1. **Hierarchical Class Structure**: Root `CulturalEntity` class provides common base for all entities, enabling flexible relationship modeling.

2. **Access Control Model**: Three-tier system (Public, Restricted, Sacred) applied to both people and cultural items, supporting fine-grained access control.

3. **Role-Based System**: Roles as separate entities allow people to have multiple roles and enable inference of specialized roles (e.g., SpiritualGuardian).

4. **Approval Workflow**: Links to TribalElder and tracks approval status, supporting cultural sensitivity requirements.

### OWL Reasoning vs SHACL Validation

#### Why does OWL reasoning automatically classify individuals as SpiritualGuardian?

OWL reasoning automatically classifies individuals as `SpiritualGuardian` because of the **equivalent-class axiom** defined in the ontology:

```
SpiritualGuardian ≡ (hasRole some Guardian) and (caresFor some SacredItem)
```

#### Why can't OWL axioms alone enforce the human approval requirement?

OWL axioms **cannot enforce constraints** like "people caring for sacred items must have human approval" because:

1. **OWL is for inference, not validation**: OWL axioms describe what **can be inferred** from existing data, not what **must be true** or what **should be rejected**
2. **OWL is monotonic**: OWL reasoning only adds new knowledge; it doesn't reject or flag invalid data
3. **Open-world assumption**: OWL assumes incomplete knowledge - missing `humanApproval` doesn't mean it's false, it means it's unknown

**What OWL CAN do**: Define that "if someone has humanApproval=true AND cares for a sacred item, then they are an ApprovedGuardian" (inference)
**What OWL CANNOT do**: Reject or flag data where "someone cares for a sacred item but humanApproval=false" (validation)

#### How does SHACL complement OWL in this scenario?

SHACL complements OWL by providing **constraint validation** that OWL cannot provide:

1. **OWL handles inference** (what can be derived):
   - Infers that people with Guardian roles caring for SacredItems are SpiritualGuardians
   - Adds new knowledge to the knowledge base

2. **SHACL handles validation** (what must be true):
   - Enforces that people caring for sacred items MUST have `humanApproval = true`
   - Reports violations when constraints are not met
   - Validates data quality and business rules

**Together**: OWL enriches the knowledge base with inferred knowledge, while SHACL ensures data quality and constraint compliance. Both are essential for a complete semantic web system.

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
