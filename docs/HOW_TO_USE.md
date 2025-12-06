# 📘 How to Use the Sudanese Relocation Recommender System

This guide explains how to run the relocation recommendation engine via:

- **Terminal (CLI)**
- **Streamlit Web App**
- **Jupyter Notebooks**

It assumes you have cloned the repository and are working inside the project root directory.

---

## 🔧 Requirements

Make sure Python 3.9+ is installed.

Install required libraries into the same Python environment that will run the project:

```bash
python -m pip install numpy pandas scikit-learn joblib streamlit

### Confirm Installation
python -m pip list
```

You should see:

- numpy
- pandas
- scikit-learn
- joblib
- streamlit

---

## 📁 Project Structure (Relevant Parts)

```powershell
Re-settlement/
├─ README.md
├─ app.py                       # Streamlit application
├─ data/
│  └─ external/
│     └─ country_features.csv
├─ notebooks/
│  ├─ intermediate/
│  │  └─ cleaned_responses.csv
│  └─ processed/
│     ├─ final_model_dataset.csv
│     ├─ final_model_dataset_with_clusters.csv
│     └─ models/
│        ├─ nn_scaler.joblib
│        └─ nn_model.joblib
└─ src/
   └─ recommendation/
      ├─ recommender.py        # Core module
      └─ cli_demo.py           # CLI interface

```

---

## 🚀 Option 1 — Run the CLI Demo

The CLI demo allows you to test recommendations directly from your terminal.

From the project root:

```bash

python -m src.recommendation.cli_demo --user-index 0 --top-k 5 --alpha 0.5

```

### Command Options

|Flag |Description |
|-------|------|
|--user-index | Which survey respondent to use (0 to N–1) |
|--top-k | Number of recommended countries|
|--alpha | Weight between heuristic and neural network score (0.0–1.0)|

You will see:

- Final blended score
- Neural network score
- Heuristic baseline score
- Human-readable explanation

---

## 💻 Option 2 — Run the Streamlit Web Application

This provides an interactive GUI in your browser.

### 1. Start Streamlit

From the project root:

```bash
python -m streamlit run app.py
```

### 2. What you can do

In the app, you can:

- Enter your age group
- Specify your estimated monthly budget (USD)
- Indicate whether you can work remotely / freelance or mainly do local/physical work
- Select one or more preferred regions (e.g., Gulf, East Africa, North Africa, Europe, Canada, USA, Asia, or Anywhere)
- Indicate whether you are actively seeking to relocate
- Indicate whether you can communicate in English
- Choose a cultural preference (Arabic-speaking, African, Western, or no strong preference)

After filling in the form, click “Generate recommendations” to:

- See a JSON view of the encoded features used by the model (for transparency)
- View a table of top recommended countries with:
- Final blended score
- Neural network score
- Heuristic baseline score
- A short explanation for each country

When launched, Streamlit will automatically open at:

```arduino
http://localhost:8501
```

---

## 🧠 Recommendation Logic

The recommendation engine ranks potential relocation destinations using a combination of:

### 1. Baseline Score (Heuristic)

A transparent, rule-based score that evaluates how well each destination matches a user's constraints and preferences. The heuristic considers:

- **Safety index**  
- **Cost of living**  
- **Presence of Sudanese diaspora**  
- **Visa accessibility for Sudanese nationals**  
- **Cultural and language compatibility**  
- **Minimum budget required compared to user budget**

This provides an interpretable and human-explainable foundation for each recommendation.

### 2. Neural Network Score (Machine Learning)

A trained multilayer perceptron (MLP) regressor predicts how suitable a destination is based on:

- Engineered survey features  
- Country-level attributes  
- Feature interactions not captured in the heuristic  

The neural network score captures non-linear relationships and emergent patterns that may not be obvious from direct rule-based scoring.

### 3. Final Blended Score

The final ranking uses a weighted combination of the heuristic and neural network scores:

```text
final_score = α * baseline_score + (1 - α) * nn_score
```

Where:

- **α** is a user-controlled blending factor  
  - `α = 1.0` → fully heuristic  
  - `α = 0.0` → fully machine learning based  
  - `α = 0.5` → equal contribution from both approaches  

### Why Blend?

- The **heuristic score** provides transparency and interpretability.  
- The **neural network score** offers flexibility and data-driven insight.  
- Blending ensures recommendations are **both explainable and adaptive**.

Users can adjust α in both the CLI and Streamlit interfaces to explore different weighting schemes.
