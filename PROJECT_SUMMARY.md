# 🌍 Sudanese Relocation Recommender System

**Personal Capstone Project — MIT Emerging Talent (ELO2)**  
**Author:** Tamir El-Waleed — 2025  

---

## 🧩 Project Overview

Due to ongoing conflict and economic instability, millions of Sudanese people continue to relocate across Africa, the Middle East, and beyond. However, selecting a relocation destination is complex and emotionally difficult. Factors such as safety, cost of living, visa requirements, employment prospects, cultural compatibility, and presence of Sudanese diaspora communities all significantly influence outcomes.

This project creates a **data-driven recommendation system** to support Sudanese individuals and families in identifying promising relocation destinations based on their personal needs, resources, and preferences.

---

## 🎯 Objectives

- **Collect structured relocation data** from Sudanese people using a 22-question online survey.
- **Engineer numeric features** reflecting experience, budget, remote-work capabilities, preferences, and constraints.
- **Combine objective country-level information** (safety, cost of living, visa accessibility, diaspora presence).
- **Build a hybrid recommendation system** using both heuristic scoring and machine learning.
- **Provide an accessible interface** via terminal (CLI) and Streamlit web application.

---

## 📊 Data Sources

- Primary data: **Google Form survey** with anonymized responses on demographic background, budget, employment, relocation goals, and constraints.
- Secondary data: Global indicators for destination countries, including:
  - Cost of living  
  - Safety index  
  - Visa policy for Sudanese nationals  
  - Presence of Sudanese diaspora  
  - Cultural and language compatibility  

Data is stored in **safe, non-identifiable format** and transformed into model-ready features.

---

## 🧠 Model Approach

The recommender produces a **ranked list of relocation destinations** using two complementary scoring methods:

1. **Heuristic baseline score**  
   Transparent domain criteria based on budget, safety, diaspora, cultural fit, and visa accessibility.

2. **Neural network score**  
   A trained MLPRegressor model predicts suitability based on learned survey patterns and country attributes.

These are blended to produce a final score:  

```text
final_score = α * baseline_score + (1 - α) * nn_score
```

Where **α** is adjustable, enabling both explainability and data-driven flexibility.

---

## 🖥️ Project Features

- **Command-line interface (`cli_demo.py`)**  
  Test recommendations for any survey respondent directly in terminal.

- **Streamlit application (`app.py`)**  
  Interactive web UI to select a user, adjust parameters, and view top relocation recommendations.

- **Well-structured codebase** (`src/`)  
  Reusable recommender functions, model loading, and scoring logic.

- **Documentation**  
  Includes full README, HOW_TO_USE guide, and variable dictionary.

---

## 🚀 Project Value & Impact

This project demonstrates that **machine learning and structured decision support** can meaningfully assist displaced populations in making informed choices during crisis. It can also:

- Support NGOs, migration services, or local community networks.
- Help families explore relocation pathways with clarity and confidence.
- Provide a foundation for future automated humanitarian tools.

The system can be expanded to include job market data, legal support resources, housing databases, sponsorship opportunities, or external immigration APIs.

---

## 🧩 Future Work

- **Deploy public web interface**
- **Add real-time visa policy data**
- **Integrate scholarships and employment API**
- **Extend survey to diaspora communities in Gulf countries and East Africa**

---

## 📬 Contact & Collaboration

If you are interested in using, reviewing, or collaborating on this project, feel free to reach out or open an issue on the GitHub repository.

[Repo Link](https://github.com/tamirwaleed/Re-settlement)  
[My LinkedIn](https://www.linkedin.com/in/tamir-el-waleed/)
