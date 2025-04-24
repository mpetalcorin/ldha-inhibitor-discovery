# Data Sheet: LDHA Inhibition Dataset

## Motivation
The dataset was created to support the development of AI models for identifying inhibitors of LDHA, an enzyme critical to the metabolism of many cancers. Inhibiting LDHA can potentially "starve" cancer cells, making this a target for anti-cancer therapies.

## Dataset Composition
- **Total Molecules**: ~2,700
- **Labels**: Active (1), Inactive (0)
- **Label Basis**: IC50 thresholds (active if < 1000 nM)
- **SMILES Format**: Canonicalized chemical structures

## Sources
- **ChEMBL**: Curated bioactivity data for LDHA targets
- **BindingDB**: IC50 values for LDHA inhibition

## Processing Steps
1. Remove duplicates and missing IC50 or SMILES
2. Normalize IC50 and convert to pChEMBL where needed
3. Label compounds as Active/Inactive
4. Apply SMOTE for balancing actives/inactives
5. Compute 1600+ Mordred descriptors (ignore 3D)
6. Feature selection using ANOVA (f_classif) to retain top 100

## Intended Use
- Model training and benchmarking
- Exploratory analysis for LDHA drug discovery
- Educational demonstrations

## Caveats
- Biological activity is based on in vitro assays
- Dataset may not generalize to unseen chemical spaces