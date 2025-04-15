# ldha-inhibitor-discovery
Machine learning pipeline to discover LDHA inhibitors
#  LDHA Drug Discovery Capstone Project

##  Project Overview

This project focuses on applying machine learning and generative AI to discover potential small molecule inhibitors targeting **Lactate Dehydrogenase A (LDHA)** — a key enzyme in cancer metabolism. By combining predictive models and generative chemistry, this pipeline identifies, scores, and ranks candidate molecules from natural product databases and AI-generated libraries.

---

##  LDHA as a Drug Target

**LDHA** plays a critical role in the Warburg effect, allowing cancer cells to survive under low oxygen by converting pyruvate to lactate. Inhibiting LDHA disrupts cancer metabolism, making it an emerging **anticancer therapeutic target**. This project leverages bioactivity data to train predictive models for LDHA inhibition.

---

##  Machine Learning Pipeline

### 1. **Dataset Sources**
- `l_lactatedehydrogenase_bioactivity_data_curated.csv` (BindingDB)
- `LDHA_inhibitors_ChemBL.csv` (ChEMBL)
- `coconut_csv-04-2025.csv` (Natural product structures)
- `chemGPT_selfies_ldha_candidates.csv` (AI-generated)

### 2. **Pipeline Steps**
- Clean and merge bioactivity datasets
- Label compounds based on pChEMBL or IC50 thresholds
- Convert SMILES into **Morgan fingerprints**
- Train and optimize models (XGBoost, Random Forest, Logistic Regression)
- Visualize SHAP values and confusion matrix
- Predict new molecules from ChemGPT/COCONUT
- Rank candidates using QED, Lipinski (RO5), toxicity, solubility, and predicted LDHA activity

---

##  Summary of Results

-  Best model: **XGBoost (Bayesian Optimized)**  
-  ROC AUC Score: **0.78** (on test set)  
-  Identified **100+ drug-like LDHA inhibitors** from natural and AI-generated molecules  
-  SHAP interpretability used to understand key fingerprint bits  
-  Visuals include confusion matrix, ROC curve, top features, and predicted molecules

---

##  Run This Project Locally

###  1. Clone the repository

git clone https://github.com/mpetalcorin/ldha-drug-discovery.git
cd ldha-drug-discovery-capstone

###  2. Install dependencies
pip install -r requirements.txt
**or using conda:**
conda env create -f environment.yml
conda activate ldha_env

###  3. Run the notebooks
**Jupyter Lab:**
jupyter lab

###  4. Run the web app
cd app
streamlit run app.py

##  Tools and Technologies Used

**ML Models:** XGBoost, RandomForest, LogisticRegression
**Feature Extraction:** RDKit (Morgan Fingerprints)
**Hyperparameter Tuning:** Optuna (Bayesian Optimization)
**Visualization:** SHAP, Matplotlib, Seaborn
**Generative Chemistry:** SELFIES, ChemGPT-style Transformer
**Web App Deployment:** Streamlit
**Data Sources:** ChEMBL, BindingDB, COCONUT, SMILES data

##  Author
**Mark Petalcorin**\
Capstone Project – AI for Drug Discovery\
*For inquiries, collaborations, or career opportunities, feel free to reach out or fork this repo!*

