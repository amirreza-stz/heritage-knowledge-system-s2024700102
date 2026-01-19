# Cultural Music Heritage Knowledge System

Final project for Social Semantic Web course (CMPE 58H) - Fall 2025

## Student Information

- **Name**: Amirreza Sattarzadeh KhanehBargh
- **Student ID**: 2024700102
- **Course**: Social Semantic Web (CMPE 58H)
- **Institution**: Boğaziçi University

## What This Project Is About

I built a knowledge system for cultural music heritage, focusing on Azerbaijani traditions like Ashiq (traditional bards) and Shaman rituals. The system uses semantic web technologies to model relationships between people, instruments, rituals, communities, and locations.

The main goal is to preserve and manage information about:
- Traditional musicians and their roles
- Cultural instruments (Baglama, Dombra, Qopuz, Shaman Saz)
- Musical works, stories, and rituals
- Community relationships and mentorship
- Access control for sensitive cultural information

## Project Structure

```
heritage-knowledge-system-s2024700102/
├── ontology/              # OWL ontology files
│   ├── s2024700102heritage.ttl
│   ├── s2024700102heritage.owl
│   └── s2024700102heritage.rdf
├── data/                  # RDF data files
│   ├── heritage_base_dataset.ttl      # Main dataset
│   ├── heritage_complete.ttl          # Ontology + data (for Protégé)
│   ├── heritage_violations_dataset.ttl # Test violations
│   ├── fixed-data.ttl                 # Corrected data
│   ├── contested-claims-reification.ttl  # Question 2: RDF reification
│   ├── contested-claims-named.trig       # Question 2: Named graphs
│   └── contested-claims-rdfstar.ttl      # Question 2: RDF-star
├── queries/               # SPARQL queries (30 total)
│   ├── q1_find_all_ashiqs.rq
│   ├── q2_find_recordings_by_location.rq
│   ├── ... (q1-q15: basic queries)
│   ├── ... (q16-q25: analytical queries)
│   ├── q1-reification.rq              # Question 2 queries
│   ├── q2-named-graphs.rq
│   ├── q3-rdfstar.rq
│   ├── q4-conflicting-claims.rq
│   └── q5-claims-by-source.rq
├── shapes/                # SHACL validation shapes
│   └── validation_shapes.ttl
├── validation/           # Validation reports and temporal constraints
│   ├── temporal-constraints.shacl     # Question 3: Temporal validation
│   ├── owl-limitation-demo.owl        # Question 3: OWL limitation demo
│   ├── base_report_final.txt          # Validation report for fixed data
│   └── violations_report.txt          # Validation report for violations
├── code/                  # Python scripts
│   ├── load-triplestore.py
│   ├── run-queries.py
│   ├── run-shacl-validation.py
│   └── export-to-gephi.py
├── screenshots/          
└── requirements.txt      # dependencies
```

## Tools and Versions

- **Protégé**: Desktop Protégé on ubuntu (latest version)
  - Used for ontology editing and testing inference
  - Reasoner: HermiT


- **Triplestore**: Apache Jena Fuseki (latest version)
  - Used for loading data and running SPARQL queries

- **Programming Language**: Python 3.7+
  - Used for SHACL validation, data processing, and Gephi export

- **Python Libraries**:
  - `rdflib >= 6.0.0` - For working with RDF data
  - `pyshacl >= 0.20.0` - For SHACL validation
  - `requests >= 2.28.0` - For HTTP requests

- **Gephi**: Latest version 

## Setup Instructions

```bash
pip install -r requirements.txt
```

- Run Protege
- Load `data/heritage_complete.ttl` for ontology viewing

- Start server for opening fuseki: `./fuseki-server`
- Open http://localhost:3030
- Create dataset and upload files

**For Question 2 (Contested Claims):**
- Load `data/contested-claims-reification.ttl` into dataset `heritage-reification`
- Load `data/contested-claims-named.trig` into dataset `heritage-named`
- Load `data/contested-claims-rdfstar.ttl` into dataset `heritage-rdfstar`


**Basic Queries (Q1-Q15)**
**Analytical Queries (Q16-Q25)**
**Question 2 Queries (for contested claims):**
- q1-reification.rq: Find high-confidence claims (reification pattern)
- q2-named-graphs.rq: Find conflicting claims (named graphs)
- q3-rdfstar.rq: Count claims per source (RDF-star)
- q4-conflicting-claims.rq: Find conflicting claims
- q5-claims-by-source.rq: Count claims by source

## Question 2: Multi-Perspective Knowledge Representation

### The Problem

Different communities have conflicting claims about cultural practices. For example, Tribe A says a ritual belongs to Lunar Cycle, while Tribe B says it belongs to Solar Cycle. I need to represent both claims with provenance (source, confidence, date) without creating logical contradictions.

### Three Implementation Patterns

**Pattern 1: RDF Reification**
- File: `data/contested-claims-reification.ttl`
- Uses `rdf:Statement` to represent claims
- Each claim has rdf:subject, rdf:predicate, rdf:object, plus metadata (source, confidence, date)
- Traditional approach, works everywhere, but verbose

**Pattern 2: Named Graphs**
- File: `data/contested-claims-named.trig`
- Each claim in a separate named graph
- Graph URI encodes metadata
- Efficient, good for provenance, but requires TriG format

**Pattern 3: RDF-star**
- File: `data/contested-claims-rdfstar.ttl`
- Uses nested triple syntax `<< >>` to annotate statements
- Clean syntax, direct annotation
- Modern approach, but requires RDF-star support


## SHACL Validation

created 12 SHACL validation shapes that check:

**Basic Validations such as:**
- Person validation: Access levels must be 1-3, human approval check
- Recording validation: Must have date, performer, location
- Cultural Item validation: Access levels and locations required
- Sacred Item validation: Must have guardian, access level 2-3
- Tribal Elder validation: Access level 3, human approval required
- Instrument validation: Location required
- Community membership: Person should belong to community
- Person roles: Person should have at least one role
- Recording access level: Complex SPARQL constraint

**Advanced Validations:**
- Mentorship validation: Mentor should have higher access level
- Approval consistency: If approvedBy exists, humanApproval must be true
- Access level hierarchy: Level 3 requires human approval
- Competency-role matching: Role-competency consistency
- Recording instrument consistency: Performer should play the instrument

### Running Validation


**to use the validation script:**
```bash
python code/run-shacl-validation.py data/heritage_base_dataset.ttl shapes/validation_shapes.ttl validation/report.txt
```

**Test with violations:**
```bash
python code/run-shacl-validation.py data/heritage_violations_dataset.ttl shapes/validation_shapes.ttl validation/report-violations.txt
```

**Question 3: Temporal constraints:**
```bash
python code/run-shacl-validation.py data/heritage_violations_dataset.ttl validation/temporal-constraints.shacl validation/violations_report.txt
python code/run-shacl-validation.py data/fixed-data.ttl validation/temporal-constraints.shacl validation/base_report_final.txt
```

## Data Overview

The `heritage_base_dataset.ttl` file contains:

- **9 Locations**: Shusha, Baku, Ganja, Nakhchivan, Qarabağ, Tabriz, Istanbul, Altai, Oslo
- **6 Communities**: Ashiq, Shaman, Musical Heritage, Ashiq Azerbaijan, Altai Shaman Lineage, Academic Research, Viking Heritage
- **20+ People**: Tribal Elders, Ashiq Masters, Shaman Masters, Guardians, Researchers, Performers
- **10+ Instruments**: Baglama, Dombra, Qopuz, Shaman Saz (some are sacred)
- **10+ Musical Works**: Traditional works like Ashig Gharib, Koroglu, Leyli and Majnoon
- **5+ Stories**: Cultural stories and narratives
- **5+ Rituals**: Traditional rituals and ceremonies
- **5+ Sacred Items**: Sacred instruments that need special access
- **10+ Recordings**: Various performances with dates, locations, and access controls

**Total**: Over 1000 triples with relationships and labels in both English and Azerbaijani

## Ontology Overview

### Main Classes

- **Person**: People in the system (with subclass TribalElder)
- **CulturalItem**: Cultural artifacts (subclasses: Instrument, MusicalWork, Recording, Ritual, Story, SacredItem)
- **Role**: Roles people can have (AshiqRole, DedeRole, GuardianRole, OzanRole, PerformerRole, ResearcherRole, ShamanRole)
- **Competency**: Skills and knowledge (InstrumentSkill, PoeticSkill, RepertoireKnowledge, RitualKnowledge, StorytellingKnowledge)
- **Community**: Cultural communities
- **Location**: Geographic locations

### Key Properties

- **Person relationships**: `hasRole`, `memberOfCommunity`, `knowsMusicalWork`, `knowsStory`, `playsInstrument`, `mentoredBy`, `performedInRitual`, `caresFor`, `hasCompetency`
- **Recording**: `performedBy`, `recordedAt`, `usesInstrument`, `recordingDate`, `restrictionEffectiveDate`
- **CulturalItem**: `locatedIn`, `isCaredForBy`, `requiresAccessLevel`
- **Access control**: `hasAccessLevel` (1-3), `humanApproval` (boolean)

## Design Decisions

### Access Control Model

I implemented a three-tier access system:
- Level 1: Public access
- Level 2: Restricted access
- Level 3: Sacred/Elder-only access

Both people and cultural items have access levels, which helps control who can access what information.

### Role-Based System

Roles are separate entities. So:
- A person can have multiple roles
- Roles can be inferred (like SpiritualGuardian)
- More flexible than making roles subclasses of Person

### OWL Reasoning vs SHACL Validation

**What OWL Can Do:**
- Infer that people with GuardianRole who care for SacredItems have SpiritualGuardian roles
- Add new knowledge to the knowledge base
- Support open-world reasoning (missing data = unknown)

**What OWL Cannot Do:**
- Enforce constraints (like "must have humanApproval")
- Reject invalid data
- Compare data property values (like dates)
- Report violations

**Example:**
```turtle
# OWL can infer:
:Person1 hasRole :GuardianRole1
:Person1 caresFor :SacredItem1
→ :GuardianRole1 rdf:type :SpiritualGuardian (inferred)

# OWL cannot enforce:
:Person1 caresFor :SacredItem1
:Person1 humanApproval false
→ OWL does NOT reject this (it's valid, just incomplete)
```

**What SHACL Can Do:**
- Enforce required properties (minCount)
- Validate data types and ranges
- Check complex constraints via SPARQL
- Report violations

**What SHACL Cannot Do:**
- Infer new knowledge
- Perform OWL reasoning
- Handle open-world assumptions

**Example:**
```turtle
# SHACL can validate:
:Person1 approvedBy :Elder1
:Person1 humanApproval false
→ SHACL reports violation: "Person approved by elder must have humanApproval = true"

# SHACL cannot infer:
:Person1 hasRole :GuardianRole1
:Person1 caresFor :SacredItem1
→ SHACL does NOT infer SpiritualGuardian (needs OWL reasoner)
```

Both are needed: OWL adds new knowledge, SHACL makes sure data is correct.

## Brief Answers to Analysis Questions

### Question 1: OWL  vs SHACL  

**Why does OWL reasoning automatically classify individuals as SpiritualGuardian?**

OWL automatically classifies individuals as SpiritualGuardian because of the equivalent-class  I defined in the ontology. It says that SpiritualGuardian is equivalent to a GuardianRole that is held by a Person who caresFor at least one SacredItem. When the reasoner runs, it checks each GuardianRole: if the person holding that role cares for a sacred item, it infers that the person is a SpiritualGuardian. This shows how OWL can derive new knowledge from existing data using logical definitions.

**Why can't OWL axioms alone enforce the human approval requirement?**

OWL can't enforce constraints like "people caring for sacred items must have human approval" because OWL is designed for inference and can not have validation. OWL uses monotonic reasoning (only adds knowledge, never rejects) and the open-world assumption (missing data means unknown, not false). OWL can infer that "if someone has humanApproval=true AND cares for a sacred item, then they are an ApprovedGuardian," but it can't reject or flag data where "someone cares for a sacred item but humanApproval=false." OWL just doesn't infer anything if conditions aren't met; it doesn't report violations.

**How does SHACL complement OWL in this scenario?**

SHACL complements OWL by providing constraint validation that OWL can't do. OWL handles inference and SHACL handles validation.
 Together, OWL enriches the knowledge base with inferred knowledge, while SHACL ensures data quality and constraint compliance. Both are needed for a complete knwoledge system.

### Question 3: OWL Limitation for Temporal Constraints 

**Why OWL Cannot Encode Temporal Access Constraints**

OWL can't enforce temporal constraints like "IF recordingDate > restrictionEffectiveDate AND performerAccessLevel < requiredAccessLevel THEN violation" for several reasons:

1. **No Date Comparisons**: OWL has no operators for comparing data property values (such as date1 > date2).

2. **No Conditional Logic**: OWL can't express "if-then" rules based on data property values.

3. **Open-World Assumption**: OWL assumes incomplete knowledge. Missing data means unknown, not false. 

4. **Monotonic Reasoning**: OWL only adds inferred knowledge; it never rejects or flags invalid data so it can't report violations.

**Fundamental Difference**: OWL uses open-world, monotonic reasoning to derive new knowledge. SHACL uses closed-world validation to enforce constraints and report violations. For temporal constraints requiring date comparisons, SHACL with SPARQL constraints is necessary. 

## Gephi Network Visualization

I added network visualization using Gephi:

1. **Export to GEXF:**
   ```bash
   python code/export-to-gephi.py data/heritage_base_dataset.ttl visualizations/heritage_network.gexf
   ```

2. **Import into Gephi:**
   - Open Gephi → File → Open → Select `visualizations/heritage_network.gexf`
   - Apply layout (I used ForceAtlas 2)
   - Color nodes by type, size by degree
   - Show node labels (not edge labels)
   - Export as PNG/SVG

## Known Limitations

1. **Date Precision**: I used `xsd:date` which has day-level precision. We could extend to `xsd:dateTime` for more precision.

2. **Access Control**: Three-tier system (1-3). Maybe could be more granular system,

3. **Approval Process**: Binary approval (true/false). Could extend 

6. **macOS Compatibility**: I had some issues running Protégé, Fuseki, and GraphDB on macOS. I used an alternative device for testing and this took lots of time and effort.

7. **my private life problems about Iran and illness and health (body and mental)**: I had so complpex time during implementation of this project and had different problems such as disconnection from my family and country with prtests and dangerous situation in Iran, also my hard illness and don't having mental and body normal health. 



## Future Improvements

- Add more equivalent-class axioms for additional inference
- Create more SHACL shapes for validation
- Optimize queries and add indexing
- Improve network visualization
- Add geographic mapping
- Link to external knowledge bases

## License

This project is for educational purposes as part of my Master's degree in Computer Engineering and Science at Boğaziçi University.

## Acknowledgments

- Azerbaijani cultural music heritage
- Ashiq tradition
- Traditional instruments and musical works
- Cultural communities and their preservation efforts
