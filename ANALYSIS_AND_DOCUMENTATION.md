# Analysis and Documentation

## Ontology Design Analysis

### Design Decisions

1. **Class Hierarchy**
   - Root class: `CulturalEntity` - provides common base for all entities
   - Main subclasses: `Person`, `CulturalItem`, `Role`, `Location`, `AccessLevel`
   - This hierarchy allows for flexible modeling of cultural heritage relationships

2. **Access Control Model**
   - Three-tier access system: Public, Restricted, Sacred
   - Both people and cultural items have access levels
   - Enables fine-grained access control for sensitive cultural information

3. **Role-Based System**
   - Roles are separate entities, allowing people to have multiple roles
   - Supports complex relationships (e.g., a person can be both Guardian and Performer)
   - Enables inference of specialized roles (e.g., SpiritualGuardian)

4. **Approval Workflow**
   - `approvedBy` property links to TribalElder
   - `humanApproval` data property tracks approval status
   - Supports cultural sensitivity requirements

### Key Relationships

1. **Care Relationships**
   - `caresFor` / `isCaredBy`: Links people to cultural items they are responsible for
   - Enables tracking of guardianship and stewardship

2. **Location Relationships**
   - `locatedIn`: Hierarchical location structure
   - `recordedAt`: Links cultural items to where they were documented

3. **Performance Relationships**
   - `performs`: Links performers to rituals
   - `playsInstrument`: Links performers to instruments
   - Supports documentation of cultural practices

## Data Structure Analysis

### Dataset Composition

- **30 People**: Diverse roles including elders, guardians, performers, archaeologists
- **50 Cultural Items**: Balanced representation across item types
- **5 Locations**: Geographic distribution
- **3 Access Levels**: Complete access control coverage

### Data Quality Features

1. **Inference Support**
   - 5 guardians with Guardian roles caring for SacredItems
   - Ready for SpiritualGuardian inference once axiom is added

2. **Validation Test Cases**
   - 2 people with `humanApproval = false` but caring for sacred items
   - 2 people with `humanApproval` but missing `hasAccessLevel`
   - Enables SHACL validation testing

## Query Analysis

### Query Categories

1. **Basic Queries**: Verification and exploration
2. **Inference Queries**: Test reasoning capabilities
3. **Validation Queries**: Data quality checks
4. **Advanced Queries**: Complex analysis and reporting

### Expected Query Results

(To be filled after running queries on another device)

## Limitations and Challenges

### Technical Limitations

1. **WebProtégé URIs**
   - Non-human-readable URIs make queries less intuitive
   - Solution: Use prefixes and labels in queries

2. **macOS Compatibility**
   - GraphDB, Fuseki, and Protégé have compatibility issues on macOS
   - Workaround: Use alternative device or virtual machine

3. **Inference Requirements**
   - Requires equivalent-class axiom to be added in Protégé
   - Cannot test inference without triplestore

### Design Limitations

1. **Date Format**
   - Uses `xsd:date` for recording dates
   - Could be extended to `xsd:dateTime` for more precision

2. **Access Control**
   - Simple three-tier system
   - Could be extended with more granular permissions

3. **Approval Process**
   - Binary approval (true/false)
   - Could be extended with approval levels or workflow states

### Challenges Encountered

1. **Tool Compatibility**
   - macOS issues with semantic web tools
   - Required workaround approach

2. **URI Management**
   - Long WebProtégé URIs make queries verbose
   - Mitigated with proper prefix usage

3. **Data Validation**
   - Manual verification required without triplestore
   - SHACL shapes created but not yet tested

## Future Improvements

1. **Enhanced Inference**
   - Add more equivalent-class axioms
   - Implement property chains for complex relationships

2. **Extended Validation**
   - More comprehensive SHACL shapes
   - Automated validation pipeline

3. **Query Optimization**
   - Index frequently queried properties
   - Optimize complex queries

4. **Documentation Enhancement**
   - Add query result examples
   - Create visualization of ontology structure
