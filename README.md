# Sudanese Relocation Recommender 🌍

![Sudanese People Relocating](https://i.guim.co.uk/img/media/e9cfa10ee80e8e60679ef01ac7bc6fe956f12405/0_315_5765_3459/master/5765.jpg?width=1900&dpr=2&s=none&crop=none)
> A data-driven recommendation system to help Sudanese individuals and families identify suitable relocation destinations based on preferences, background, and humanitarian context.

---

## Table of Contents

- [Sudanese Relocation Recommender 🌍](#sudanese-relocation-recommender-)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Motivation \& Background](#motivation--background)
    - [Historical Context: Long-standing Crisis in Darfur \& Pre-War Migration](#historical-context-long-standing-crisis-in-darfur--pre-war-migration)
    - [2023 Conflict Escalation \& Unprecedented Displacement](#2023-conflict-escalation--unprecedented-displacement)
    - [Displacement Patterns \& Host Countries](#displacement-patterns--host-countries)
    - [Why a Data-Driven Relocation Recommender is Needed](#why-a-data-driven-relocation-recommender-is-needed)
    - [🔗 Key Sources \& Data References](#-key-sources--data-references)
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

### Historical Context: Long-standing Crisis in Darfur & Pre-War Migration

Displacement in Sudan did not begin in 2023 — it has been unfolding for over two decades. In February 2003, the Darfur conflict erupted, when rebel groups challenged marginalization and state policies in western Sudan, triggering a brutal counterinsurgency by government forces and allied militias. The violence included widespread human rights abuses, village destruction, sexual violence, mass killings, and ethnic cleansing. ([War in Darfur — Wikipedia](https://en.wikipedia.org/wiki/War_in_Darfur?utm_source=chatgpt.com))  

By the mid-2000s, the Darfur crisis had already displaced **around 2 million people internally** and pushed hundreds of thousands to neighboring countries such as Chad. ([Human Rights Watch report](https://www.hrw.org/reports/2007/sudan0907/sudan0907webtext.pdf?utm_source=chatgpt.com))  
Even prior to the 2023 civil war, Sudanese people were relocating due to decades of economic instability, localized conflicts, and systemic underdevelopment. Many settled in Egypt, Saudi Arabia, the Gulf states, Uganda, and Kenya, establishing early diaspora networks that continue to influence migration decisions today.

### 2023 Conflict Escalation & Unprecedented Displacement

On 15 April 2023, full-scale hostilities erupted between the Sudanese Armed Forces (SAF) and the Rapid Support Forces (RSF), plunging Sudan into a nationwide war. This “power struggle” between rival military factions has devastated civilian life, infrastructure, and basic services. ([Council on Foreign Relations — Sudan Conflict Tracker](https://www.cfr.org/global-conflict-tracker/conflict/power-struggle-sudan?utm_source=chatgpt.com))  

By late 2024 and into 2025, Sudan had become the world’s largest displacement crisis. According to UNHCR, **more than 11.8 million Sudanese have been forcibly displaced**, including **over 11.5 million internally displaced persons (IDPs)**. ([UNHCR Sudan Situation](https://data.unhcr.org/en/situations/sudansituation?utm_source=chatgpt.com))  
Millions have crossed borders — primarily into **Chad, Egypt, South Sudan, Ethiopia, Uganda, and the Central African Republic** — while others have moved to Gulf and North African countries via diaspora channels. ([UNHCR Country Data: Sudan](https://data.unhcr.org/en/country/sdn?utm_source=chatgpt.com))  

This is not just a numbers crisis — it is a humanitarian catastrophe affecting livelihoods, access to food, healthcare, water, sanitation, education, and economic survival. International media have described Sudan as one of “the worst humanitarian nightmares in recent history.” ([ABC News — Sudan crisis report](https://abcnews.go.com/International/sudan-now-worst-humanitarian-nightmares-recent-history/story?id=104173197))

### Displacement Patterns & Host Countries

Several significant relocation trends are emerging:

- **Border displacement:** Rapid mass movements to Sudan’s land borders, especially Chad and South Sudan, captured by displacement tracking tools and border monitoring. ([IOM DTM — “One Year of Conflict in Sudan”](https://dtm.iom.int/online-interactive-resources/one-year-conflict-sudan-visualizing-worlds-largest-displacement-crisis))  
  
- **Urban–urban displacement:** Movement from major cities (Khartoum, Omdurman) to relatively safer urban centers (Port Sudan, Wad Madani) before secondary migration abroad.  
- **Gulf migration & labor relocation:** Long-standing Sudanese economic migration into Saudi Arabia, UAE, and Qatar — with new humanitarian dimensions after 2023. ([CMI — Saudi Arabia and Sudanese refugees](https://www.cmi.no/publications/8834-saudi-arabia-and-sudanese-refugees))

Migration decisions today reflect a mix of crisis-driven displacement and pre-existing diaspora structures — shaping who relocates, where they relocate, and how they integrate.

### Why a Data-Driven Relocation Recommender is Needed

Sudanese individuals and families face complex decisions regarding relocation: weighing **safety, economic opportunity, family needs, visa access, community connection, and cost of living**, often under extreme pressure and uncertainty.  
These decisions are typically based on informal information — personal networks, social media, or anecdotal advice — rather than systematic, transparent, data-driven analysis.

A recommendation system powered by survey data and external indicators can help by:

- Mapping user preferences to country profiles  
- Prioritizing key dimensions (safety, legal access, socioeconomic viability, community presence)  
- Producing ranked relocation suggestions with interpretability and explanation  
- Providing a consistent, replicable decision support tool for vulnerable populations  

This project aims to combine **individual constraints** (family size, budget, visa status), **personal priorities** (safety, employment, education, community), and **country-level data** (security, cost of living, diaspora presence, immigration feasibility) to generate **personalized relocation recommendations** for Sudanese users.

---

### 🔗 Key Sources & Data References

| Source| Focus |
|-------|------|
| [Council on Foreign Relations — Conflict Tracker](https://www.cfr.org/global-conflict-tracker/conflict/power-struggle-sudan) | Overview of SAF–RSF power struggle and current conflict drivers |
| [UNHCR — Sudan Situation Dashboard](https://data.unhcr.org/en/situations/sudansituation)| Live displacement data, refugee flows, host countries |
| [UNHCR — Sudan Country Profile](https://data.unhcr.org/en/country/sdn) | Historical refugee context and internal displacement |
| [CMI — Sudanese Refugees in Saudi Arabia](https://www.cmi.no/publications/8834-saudi-arabia-and-sudanese-refugees) | Gulf migration, integration, identity and policy study |
| [ABC News — Humanitarian Nightmare Article](https://abcnews.go.com/International/sudan-now-worst-humanitarian-nightmares-recent-history/story?id=104173197) | Qualitative severity of humanitarian crisis |
| [IOM DTM — Visual Displacement Dashboard](https://dtm.iom.int/online-interactive-resources/one-year-conflict-sudan-visualizing-worlds-largest-displacement-crisis) | Internal displacement, border movements, data visualization |
| [Human Rights Watch — Darfur Report](https://www.hrw.org/reports/2007/sudan0907/sudan0907webtext.pdf) | Evidence of pre-2023 mass displacement |

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
