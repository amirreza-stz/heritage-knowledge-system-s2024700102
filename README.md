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

The project includes 10 SPARQL queries:

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

## SHACL Validation

The SHACL shapes validate:

- **Person validation**: Access levels (1-3), human approval
- **Recording validation**: Required dates, performers, locations
- **Cultural Item validation**: Access levels, locations
- **Sacred Item validation**: Must have guardians, access level 3
- **Tribal Elder validation**: Access level 3, human approval required
- **Date consistency**: Recording dates vs restriction dates

## Sample Data

The `heritage_base_dataset.ttl` includes:

- **5 Locations**: Shusha, Baku, Ganja, Nakhchivan, Qarabağ
- **3 Communities**: Ashiq, Shaman, Musical Heritage
- **6 People**: Tribal Elder, 2 Ashiq Masters, Shaman Master, Guardian, Researcher, Performer
- **6 Instruments**: Baglama, Dombra, Qopuz, Shaman Saz
- **4 Musical Works**: Ashig Gharib, Koroglu, Leyli and Majnoon, Shaman Ritual Song
- **2 Stories**: Ashig Gharib Story, Koroglu Story
- **2 Rituals**: Spring Ritual, Harvest Ritual
- **2 Sacred Items**: Sacred Baglama, Sacred Qopuz
- **5 Recordings**: Various performances with dates and locations

## Contributing

This is a course project for Social Semantic Web. For questions or improvements, please contact the project maintainer.

## License

This project is created for educational purposes as part of a Master's degree program in Computer Engineering and Science.

## Acknowledgments

- Azerbaijani cultural music heritage
- Ashiq tradition
- Traditional instruments and musical works
