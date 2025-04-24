# Model Card: LDHA Inhibitor Classifier

## Overview
This model predicts whether a given molecule (represented by its SMILES string) is likely to inhibit the LDHA enzyme, which plays a key role in cancer metabolism. It was trained using LightGBM on bioactivity data labeled as active or inactive.

## Intended Use
This model is intended for:
- Early-stage virtual screening of potential LDHA inhibitors.
- Educational purposes in cheminformatics and bioactivity prediction.

Not intended for:
- Clinical decision-making.
- Replacing experimental validation.

## Training Data
**Sources**: BindingDB and ChEMBL  
**Dataset**: `LDHA_inhibitors_SMOTE_balanced_with_SMILES.csv`  
**Samples**: ~2,700 molecules with known LDHA activity and IC50 values.  
**Class Balance**: Balanced using SMOTE (Synthetic Minority Oversampling Technique)  
**Features**: Mordred descriptors (~1,600 calculated, top 100 selected via `f_classif`)

## Model Details
- **Type**: LightGBM Classifier
- **Validation**: 5-Fold Cross-Validation
- **Best AUC Score**: 0.991
- **Test Accuracy**: >96%
- **Input**: 100 Mordred descriptors (numerical)
- **Output**: Binary classification (Active/Inactive) and LDHA inhibition probability

## Interpretability
- SHAP used to interpret feature contributions
- Important features include top physicochemical and structural properties

## Limitations
- Performance may drop on completely novel chemical spaces
- Assumes quality SMILES input and drug-likeness

## Ethical Considerations
- Should not be used to guide treatment decisions without experimental validation.