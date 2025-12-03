# Sudanese Relocation Recommender 🌍

![Sudanese People Relocating](https://i.guim.co.uk/img/media/e9cfa10ee80e8e60679ef01ac7bc6fe956f12405/0_315_5765_3459/master/5765.jpg?width=1900&dpr=2&s=none&crop=none)
> A data-driven recommendation system to help Sudanese individuals and families identify suitable relocation destinations based on preferences, background, and humanitarian context.

---

## Table of Contents

- [Sudanese Relocation Recommender 🌍](#sudanese-relocation-recommender-)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Motivation \& Background](#motivation--background)
    - [Humanitarian Context \& Sudan War](#humanitarian-context--sudan-war)
    - [Why Relocation Recommendation Matters](#why-relocation-recommendation-matters)
  - [Objectives \& Research Questions](#objectives--research-questions)
  - [Data Collection \& Survey Design](#data-collection--survey-design)
  - [Data Pipeline \& Methodology](#data-pipeline--methodology)
  - [System Architecture / Repo Structure](#system-architecture--repo-structure)
  - [Getting Started](#getting-started)
    - [How to run](#how-to-run)
  - [Usage / Example](#usage--example)
  - [Limitations \& Ethics / Bias Considerations](#limitations--ethics--bias-considerations)
  - [Future Work / Roadmap](#future-work--roadmap)
  - [Contributors](#contributors)

---

## Project Overview

This project aims to build a machine-learning powered recommendation system tailored for Sudanese individuals/families seeking to relocate — whether due to conflict, economic hardship, or other humanitarian reasons. By combining survey data with relevant socioeconomic, safety, and opportunity indicators across potential destination countries, the system will output a ranked list of recommended locations (countries / cities), along with explanations for why each destination matches the user’s preferences and circumstances.

---

## Motivation & Background

### Humanitarian Context & Sudan War

Sudan — like many conflict-affected countries — has been subjected to prolonged political instability, armed conflict, and humanitarian crises. These events have caused mass displacement internally and internationally, disrupting livelihoods, safety, and access to basic services. *[Here you will insert a brief literature review summarizing key facts about the conflict, refugee flows, economic collapse, and international migration patterns relevant to Sudan]*.  

Relocating — whether internally or abroad — is often one of the few ways for individuals and families to seek safety, stability, and opportunities. However, relocation decisions are complex, involving trade-offs between safety, socioeconomic opportunities, community support, costs, and personal preferences.  

### Why Relocation Recommendation Matters

- Many potential migrants have limited information about which destinations might offer the best balance of **safety**, **employment prospects**, **community support**, **cost of living**, and **social integration**.  
- A data-driven recommender can help reduce uncertainty. By combining individual preferences/constraints with objective indicators, it offers more informed, personalized relocation suggestions.  
- For displaced populations and humanitarian actors, such a tool could support better decision-making, planning, and support services — ensuring relocations are safer, more sustainable, and aligned with individual needs.

---

## Objectives & Research Questions

- **Main goal**: Build a recommender system that suggests optimal relocation destinations for Sudanese individuals/families based on their background, preferences, constraints, and risk profile.  
- **Research questions**:  
    1. Which features (e.g., safety, cost of living, job availability, cultural/language proximity, community presence) are most influential in relocation suitability?  
    2. How to model trade-offs between sometimes conflicting factors (e.g., safety vs. cost of living)?  
    3. How to ensure fairness and avoid bias when recommending destinations (avoiding over- or under-recommendation of certain countries)?  
    4. How to translate raw user survey responses into meaningful, comparable features across countries?  

---

## Data Collection & Survey Design

- Survey is implemented via a form (e.g., Google Form) targeting Sudanese respondents. It collects demographic information, family status, relocation motivations, preferences (climate, language, work sector, safety, social/community network, cost-sensitivity, etc.), constraints (visa, budget, family obligations), and subjective priorities (safety, livelihood, community, education, etc.).  
- After export, survey responses will be anonymized and stored as CSV in the `data/raw/` folder.  
- We will complement survey data with external country-level / city-level socioeconomic datasets (e.g. cost-of-living indexes, employment rates, refugee integration indices, safety/crime data, language similarity, diaspora/community presence).  

*(More details including variable definitions, data sources, and mapping logic will be documented separately in `docs/variable_dictionary.md` and `docs/survey_design.md`.)*

---

## Data Pipeline & Methodology

1. **Data cleaning & preprocessing** — Remove invalid entries, encode categorical responses, handle missing data.  
2. **Feature engineering** — Combine survey responses + external country/city data to build a unified feature matrix for each candidate relocation destination per user profile.  
3. **Modeling / Recommendation logic** — Experiment with one or more of:  
   - Ranking algorithms (e.g. weighted-scoring, multi-criteria decision analysis),  
   - Clustering (to segment users and match to country clusters),  
   - Hybrid ML + rule-based system that balances quantitative and qualitative factors.  
4. **Evaluation** — Since “ground-truth” labels are hard, evaluation will be partly qualitative: simulate user-profiles and assess whether recommendations make sense; get feedback from peers / domain experts.  
5. **Deployment / Inference** — Build a simple interface (e.g. a web app or command-line tool) to capture user inputs and output recommended destinations + explanation.  

---

## System Architecture / Repo Structure

```text
<top-level folders>  
data/  
notebooks/  
src/  
models/  
reports/  
figures/  
docs/  
app/  
```

---

## Getting Started

Prerequisites

Python ≥ 3.9

(Optional) Virtual environment (venv / conda)

Installation

``` bash
git clone <repo-url>
cd sudan-relocation-recommender
python -m venv venv
source venv/bin/activate   # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt
```

### How to run

- Use notebooks under notebooks/ for data exploration and model experimentation.

- Use src/ modules (e.g. src/data_processing/load_data.py, src/models/train_model.py, etc.) for reproducible processing/pipeline.

- After training a model, run app/streamlit_app.py (or equivalent) to get relocation recommendations for a new user profile.

---

## Usage / Example

---

## Limitations & Ethics / Bias Considerations

---

## Future Work / Roadmap

---

## Contributors

---
