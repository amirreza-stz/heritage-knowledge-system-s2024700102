# Cultural Music Heritage Knowledge System

A comprehensive knowledge system for managing and preserving Cultural Music Heritage in Azerbaijan and similar cultures, built using Semantic Web technologies.

## Project Overview

This project implements an ontology-based knowledge system for cultural music heritage, focusing on:
- **Ashiq** (traditional Azerbaijani bards) and their musical traditions
- **Shaman** rituals and practices
- Traditional instruments (Baglama, Dombra, Qopuz, Shaman Saz)
- Musical works, stories, and rituals
- Community relationships and mentorship
- Cultural preservation and access control

## Project Structure

```
heritage-knowledge-system-s2024700102/
├── ontology/              # OWL ontology files
│   ├── s2024700102heritage.ttl
│   ├── s2024700102heritage.owl
│   └── s2024700102heritage.rdf
├── data/                  # RDF data files
│   ├── heritage_base_dataset.ttl      # Comprehensive dataset (merged and enhanced)
│   ├── heritage_violations_dataset.ttl # Intentional violations for testing
│   └── DATA_MERGE_SUMMARY.md          # Dataset documentation
├── queries/               # SPARQL queries
│   ├── q1_find_all_ashiqs.rq
│   ├── q2_find_recordings_by_location.rq
│   └── ... (10 queries total)
├── shapes/                # SHACL validation shapes
│   └── validation_shapes.ttl
├── code/                  # Python scripts
│   ├── load-triplestore.py
│   ├── run-queries.py
│   └── run-shacl-validation.py
├── validation/           # Validation reports
├── screenshots/           # Screenshots for documentation
└── requirements.txt      # Python dependencies
```

## Ontology Overview

### Main Classes

- **Person**: People in the cultural heritage system (with subclass TribalElder)
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

## Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up a triplestore** (choose one):
   - **Apache Jena Fuseki**: Download from https://jena.apache.org/download/
   - **GraphDB**: Download from https://www.ontotext.com/products/graphdb/

## Usage

### 1. Load Data into Triplestore

**Using Fuseki Web UI (Recommended):**
1. Start Fuseki: `./fuseki-server`
2. Open: http://localhost:3030
3. Create a new dataset (e.g., `heritage`)
4. Upload files in this order:
   - **Option A (Recommended)**: `data/heritage_complete.ttl` (ontology + data combined)
   - **Option B**: 
     - `ontology/s2024700102heritage.ttl` (ontology first)
     - `data/heritage_base_dataset.ttl` (data second)

**Using command line:**
```bash
python code/load-triplestore.py heritage data/heritage_base_dataset.ttl
```

### 2. Run SPARQL Queries

**Using Fuseki Web UI:**
1. Navigate to your dataset
2. Click "Query" tab
3. Copy and paste queries from `queries/` directory
4. Execute and view results

**Using command line:**
```bash
python code/run-queries.py http://localhost:3030/heritage/sparql
```

This will execute all queries in the `queries/` directory and save results to `queries/results/`.

### 3. Validate Data with SHACL

**Run validation:**
```bash
python test_shacl.py
```

**Or use the validation script:**
```bash
python code/run-shacl-validation.py data/heritage_base_dataset.ttl shapes/validation_shapes.ttl validation/report.txt
```

**Test with violations:**
```bash
python code/run-shacl-validation.py data/heritage_violations_dataset.ttl shapes/validation_shapes.ttl validation/report-violations.txt
```

## SPARQL Queries

The project includes **25 SPARQL queries** organized into two categories:

### Basic Information Retrieval (Q1-Q15)

1. **q1_find_all_ashiqs.rq**: Find all Ashiq performers and their instruments
2. **q2_find_recordings_by_location.rq**: Find recordings by location
3. **q3_find_sacred_items_guardians.rq**: Find sacred items and their guardians
4. **q4_find_people_by_competency.rq**: Find people with specific competencies
5. **q5_find_mentorship_relationships.rq**: Find mentorship relationships
6. **q6_find_ritual_participants.rq**: Find ritual participants
7. **q7_find_community_members.rq**: Find community members
8. **q8_find_musical_works_by_location.rq**: Find musical works by location
9. **q9_find_approved_persons.rq**: Find persons approved by tribal elders
10. **q10_find_recordings_with_instruments.rq**: Find recordings with instruments
11. **q11_find_spiritual_guardians.rq**: Find SpiritualGuardians (inferred via OWL)
12. **q12_find_people_by_access_level.rq**: Find people by access level
13. **q13_find_cultural_items_by_location.rq**: Find cultural items by location
14. **q14_find_people_with_multiple_roles.rq**: Find people with multiple roles
15. **q15_find_recordings_with_access_violations.rq**: Find recordings with access violations

### Analytical Queries (Q16-Q25)

16. **q16_statistics_overview.rq**: Overall statistics (counts of entities)
17. **q17_access_level_distribution.rq**: Access level distribution analysis
18. **q18_community_analysis.rq**: Community membership analysis
19. **q19_temporal_analysis.rq**: Temporal analysis of recordings
20. **q20_guardian_analysis.rq**: Spiritual guardian analysis
21. **q21_mentorship_network.rq**: Mentorship network mapping
22. **q22_instrument_usage_analysis.rq**: Instrument usage analysis
23. **q23_location_cultural_density.rq**: Cultural density by location
24. **q24_approval_network.rq**: Approval network analysis
25. **q25_comprehensive_validation_check.rq**: Comprehensive validation check

See `ANALYTICAL_QUESTIONS.md` for detailed documentation of all queries.

## SHACL Validation

The SHACL shapes include **12 validation shapes** that validate:

### Basic Validations (9 shapes)
- **Person validation**: Access levels (1-3), human approval
- **Recording validation**: Required dates, performers, locations
- **Cultural Item validation**: Access levels, locations
- **Sacred Item validation**: Must have guardians, access level 2-3
- **Tribal Elder validation**: Access level 3, human approval required
- **Instrument validation**: Location requirements
- **Community membership**: Person should belong to community
- **Person roles**: Person should have at least one role
- **Recording access level**: Complex SPARQL constraint for access validation

### Advanced Validations (3 shapes)
- **Mentorship validation**: Mentor access level hierarchy
- **Approval consistency**: Approval and humanApproval alignment
- **Access level hierarchy**: Access level 3 requirements
- **Competency-role matching**: Role-competency consistency
- **Recording instrument consistency**: Performer-instrument matching

See `VALIDATION_VIOLATIONS_GUIDE.md` for detailed validation documentation.

## Sample Data

The `heritage_base_dataset.ttl` includes:

- **9 Locations**: Shusha, Baku, Ganja, Nakhchivan, Qarabağ, Tabriz, Istanbul, Altai, Oslo
- **6 Communities**: Ashiq, Shaman, Musical Heritage, Ashiq Azerbaijan, Altai Shaman Lineage, Academic Research, Viking Heritage
- **20+ People**: Tribal Elders, Ashiq Masters, Shaman Masters, Guardians, Researchers, Performers
- **10+ Instruments**: Baglama, Dombra, Qopuz, Shaman Saz (including sacred instruments)
- **10+ Musical Works**: Traditional works including Ashig Gharib, Koroglu, Leyli and Majnoon
- **5+ Stories**: Cultural stories and narratives
- **5+ Rituals**: Traditional rituals and ceremonies
- **5+ Sacred Items**: Sacred instruments requiring special access
- **10+ Recordings**: Various performances with dates, locations, and access controls

**Total**: 1000+ triples with comprehensive relationships and bilingual labels (English/Azerbaijani)

See `DATA_ANALYSIS.md` for detailed data analysis and design decisions.

## Key Design Decisions

### 1. Hierarchical Class Structure
- Root class `CulturalEntity` provides common base for all entities
- Enables flexible relationship modeling and inheritance

### 2. Access Control Model
- Three-tier system (1: Public, 2: Restricted, 3: Sacred/Elder-only)
- Applied to both people and cultural items
- Supports fine-grained access control

### 3. Role-Based System
- Roles as separate entities (instances, not classes)
- Enables multiple roles per person
- Supports OWL inference (e.g., `SpiritualGuardian`)

### 4. OWL Reasoning vs SHACL Validation
- **OWL**: Infers new knowledge (e.g., SpiritualGuardian roles)
- **SHACL**: Validates constraints and data quality
- Both are essential for a complete semantic web system

See `DATA_ANALYSIS.md` for comprehensive analysis of design decisions.

## Visualization

### Gephi Network Visualization

The project includes network visualization capabilities:

1. **Export to GEXF:**
   ```bash
   python code/export-to-gephi.py data/heritage_base_dataset.ttl visualizations/heritage_network.gexf
   ```

2. **Import into Gephi:**
   - Open Gephi → File → Open → Select `visualizations/heritage_network.gexf`
   - Apply layout (e.g., ForceAtlas 2)
   - Color nodes by type, size by degree
   - Export as PNG/SVG

See `GEPHI_VISUALIZATION_GUIDE.md` for detailed instructions.

## Documentation

- **`DATA_ANALYSIS.md`**: Comprehensive data analysis and design decisions
- **`ANALYTICAL_QUESTIONS.md`**: Documentation of all 25 queries
- **`VALIDATION_VIOLATIONS_GUIDE.md`**: Validation violations guide
- **`PROJECT_COMPLETION_FINAL.md`**: Complete project status
- **`QUICK_REFERENCE.md`**: Quick reference guide

## Limitations and Future Improvements

### Current Limitations
- Date precision: Uses `xsd:date` (could extend to `xsd:dateTime`)
- Access control: Three-tier system (could be more granular)
- Approval process: Binary (could extend with workflow states)

### Future Improvements
- Enhanced inference with more equivalent-class axioms
- Extended SHACL validation with comprehensive shapes
- Query optimization and indexing
- Network visualization enhancements
- Geographic mapping integration

## Contributing

This is a course project for Social Semantic Web. For questions or improvements, please contact the project maintainer.

## License

This project is created for educational purposes as part of a Master's degree program in Computer Engineering and Science.

## Acknowledgments

- Azerbaijani cultural music heritage
- Ashiq tradition
- Traditional instruments and musical works
- Cultural communities and their preservation efforts