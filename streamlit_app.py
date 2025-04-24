import streamlit as st
import pandas as pd
import numpy as np
import joblib
from rdkit import Chem
from rdkit.Chem import Descriptors, Crippen, QED
from mordred import Calculator, descriptors
import warnings

warnings.filterwarnings("ignore")

# --- Load model and preprocessing tools ---
model = joblib.load("models/ldha_lightgbm_model.pkl")
scaler = joblib.load("models/scaler.pkl")
selector = joblib.load("models/selector.pkl")
descriptor_names = joblib.load("models/descriptor_names.pkl")

# --- Streamlit Page Setup ---
st.set_page_config(page_title="LDHA Inhibitor Prediction", layout="wide")
st.title("LDHA Inhibitor Predictor")
st.markdown("""
Upload SMILES strings to check if they are potential **LDHA inhibitors**.
We’ll also compute drug-likeness scores like QED, LogP, MW, TPSA and Lipinski RO5.
""")

# --- Sidebar Input ---
smiles_input = st.text_area("Paste SMILES (one per line):", height=200)

# --- Helper Functions ---
def compute_descriptors(smiles_list):
    calc = Calculator(descriptors, ignore_3D=True)
    mols, valid_smiles = [], []
    for smi in smiles_list:
        mol = Chem.MolFromSmiles(smi)
        if mol:
            mols.append(mol)
            valid_smiles.append(smi)
    descs = [calc(m).fill_missing(0).asdict() for m in mols]
    return pd.DataFrame(descs), valid_smiles, mols

def druglikeness_properties(mol):
    mw = Descriptors.MolWt(mol)
    logp = Crippen.MolLogP(mol)
    qed = QED.qed(mol)
    tpsa = Descriptors.TPSA(mol)
    ro5 = int((mw > 500) + (logp > 5) + (Descriptors.NumHDonors(mol) > 5) + (Descriptors.NumHAcceptors(mol) > 10))
    return mw, logp, qed, tpsa, ro5

# --- Prediction Logic ---
if st.button("Predict"):
    if smiles_input.strip():
        smiles_list = [s.strip() for s in smiles_input.splitlines() if s.strip()]
        desc_df, valid_smiles, mols = compute_descriptors(smiles_list)

        if len(valid_smiles) == 0:
            st.warning("No valid SMILES found.")
        else:
            try:
                desc_df = desc_df[descriptor_names]
                desc_scaled = scaler.transform(desc_df)
                desc_selected = selector.transform(desc_scaled)

                preds = model.predict(desc_selected)
                probs = model.predict_proba(desc_selected)[:, 1]

                results = []
                for i, smi in enumerate(valid_smiles):
                    mw, logp, qed, tpsa, ro5 = druglikeness_properties(mols[i])
                    results.append({
                        "SMILES": smi,
                        "LDHA_Prob": round(probs[i], 3),
                        "Prediction": "Active" if preds[i] == 1 else "Inactive",
                        "QED": round(qed, 3),
                        "LogP": round(logp, 3),
                        "MW": round(mw, 1),
                        "TPSA": round(tpsa, 1),
                        "RO5_Violations": ro5
                    })

                df_results = pd.DataFrame(results)
                st.success(f"Predicted {len(df_results)} molecules.")
                st.dataframe(df_results)
                csv = df_results.to_csv(index=False).encode("utf-8")
                st.download_button("Download Results", data=csv, file_name="ldha_predictions.csv", mime="text/csv")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please input SMILES.")
