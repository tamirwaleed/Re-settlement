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
    - [Why Relocation Recommendation Matters](#why-relocation-recommendation-matters)
  - [Objectives \& Research Questions](#objectives--research-questions)
    - [Project Goal](#project-goal)
    - [Core Objectives](#core-objectives)
    - [Research Questions](#research-questions)
    - [Hypothesis (Working Assumption)](#hypothesis-working-assumption)
    - [Expected Outcomes](#expected-outcomes)
  - [Data Collection \& Survey Design](#data-collection--survey-design)
  - [Data Collection and Survey Design](#data-collection-and-survey-design)
    - [Survey Categories and Feature Rationale](#survey-categories-and-feature-rationale)
    - [Data Handling and Processing Approach](#data-handling-and-processing-approach)
    - [Data Structure in the Repository](#data-structure-in-the-repository)
  - [Data Pipeline \& Methodology](#data-pipeline--methodology)
  - [System Architecture / Repo Structure](#system-architecture--repo-structure)
  - [Recommendation Logic and Modelling Approach](#recommendation-logic-and-modelling-approach)
    - [Step 1. Rule Based Eligibility Filter](#step-1-rule-based-eligibility-filter)
    - [Step 2. Unsupervised Clustering](#step-2-unsupervised-clustering)
      - [2.1 Clustering respondents](#21-clustering-respondents)
      - [2.2 Clustering destinations](#22-clustering-destinations)
    - [Step 3. Supervised Learning with a Neural Network](#step-3-supervised-learning-with-a-neural-network)
      - [3.1 Input representation](#31-input-representation)
      - [3.2 Labels and training strategy](#32-labels-and-training-strategy)
      - [3.3 Network architecture (initial version)](#33-network-architecture-initial-version)
    - [Step 4. K Fold Cross Validation](#step-4-k-fold-cross-validation)
    - [Step 5. Final Recommendation and Explanation](#step-5-final-recommendation-and-explanation)
  - [Getting Started](#getting-started)
  - [Limitations and Ethics](#limitations-and-ethics)
    - [1. No model can guarantee a successful relocation](#1-no-model-can-guarantee-a-successful-relocation)
    - [2. Data availability and quality limitations](#2-data-availability-and-quality-limitations)
    - [3. Ethical handling of sensitive attributes](#3-ethical-handling-of-sensitive-attributes)
    - [4. Partial and proxy labeling for supervised learning](#4-partial-and-proxy-labeling-for-supervised-learning)
    - [5. Risk of algorithmic bias](#5-risk-of-algorithmic-bias)
    - [6. Changing humanitarian conditions](#6-changing-humanitarian-conditions)
    - [7. Human responsibility and agency](#7-human-responsibility-and-agency)
    - [8. Transparency and documentation](#8-transparency-and-documentation)
    - [9. Ethical review for deployment](#9-ethical-review-for-deployment)

---

## Project Overview

This project aims to build a machine-learning powered recommendation system tailored for Sudanese individuals/families seeking to relocate: whether due to conflict, economic hardship, or other humanitarian reasons. By combining survey data with relevant socioeconomic, safety, and opportunity indicators across potential destination countries, the system will output a ranked list of recommended locations (countries / cities), along with explanations for why each destination matches the user’s preferences and circumstances.

---

## Motivation & Background

### Historical Context: Long-standing Crisis in Darfur & Pre-War Migration

Displacement in Sudan did not begin in 2023: it has been unfolding for over two decades. In February 2003, the Darfur conflict erupted, when rebel groups challenged marginalization and state policies in western Sudan, triggering a brutal counterinsurgency by government forces and allied militias. The violence included widespread human rights abuses, village destruction, sexual violence, mass killings, and ethnic cleansing. ([War in Darfur: Wikipedia](https://en.wikipedia.org/wiki/War_in_Darfur))  

By the mid-2000s, the Darfur crisis had already displaced **around 2 million people internally** and pushed hundreds of thousands to neighboring countries such as Chad. ([Human Rights Watch report](https://www.hrw.org/reports/2007/sudan0907/sudan0907webtext.pdf))  
Even prior to the 2023 civil war, Sudanese people were relocating due to decades of economic instability, localized conflicts, and systemic underdevelopment. Many settled in Egypt, Saudi Arabia, the Gulf states, Uganda, and Kenya, establishing early diaspora networks that continue to influence migration decisions today.

### 2023 Conflict Escalation & Unprecedented Displacement

On 15 April 2023, full-scale hostilities erupted between the Sudanese Armed Forces (SAF) and the Rapid Support Forces (RSF), plunging Sudan into a nationwide war. This “power struggle” between rival military factions has devastated civilian life, infrastructure, and basic services. ([Council on Foreign Relations: Sudan Conflict Tracker](https://www.cfr.org/global-conflict-tracker/conflict/power-struggle-sudan))  

By late 2024 and into 2025, Sudan had become the world’s largest displacement crisis. According to UNHCR, **more than 11.8 million Sudanese have been forcibly displaced**, including **over 11.5 million internally displaced persons (IDPs)**. ([UNHCR Sudan Situation](https://data.unhcr.org/en/situations/sudansituation))  
Millions have crossed borders: primarily into **Chad, Egypt, South Sudan, Ethiopia, Uganda, and the Central African Republic**: while others have moved to Gulf and North African countries via diaspora channels. ([UNHCR Country Data: Sudan](https://data.unhcr.org/en/country/sdn))  

This is not just a numbers crisis: it is a humanitarian catastrophe affecting livelihoods, access to food, healthcare, water, sanitation, education, and economic survival. International media have described Sudan as one of “the worst humanitarian nightmares in recent history.” ([ABC News: Sudan crisis report](https://abcnews.go.com/International/sudan-now-worst-humanitarian-nightmares-recent-history/story?id=104173197))

### Displacement Patterns & Host Countries

Several significant relocation trends are emerging:

- **Border displacement:** Rapid mass movements to Sudan’s land borders, especially Chad and South Sudan, captured by displacement tracking tools and border monitoring. ([IOM DTM: “One Year of Conflict in Sudan”](https://dtm.iom.int/online-interactive-resources/one-year-conflict-sudan-visualizing-worlds-largest-displacement-crisis))  
  
- **Urban–urban displacement:** Movement from major cities (Khartoum, Omdurman) to relatively safer urban centers (Port Sudan, Wad Madani) before secondary migration abroad.  
- **Gulf migration & labor relocation:** Long-standing Sudanese economic migration into Saudi Arabia, UAE, and Qatar: with new humanitarian dimensions after 2023. ([CMI: Saudi Arabia and Sudanese refugees](https://www.cmi.no/publications/8834-saudi-arabia-and-sudanese-refugees))

Migration decisions today reflect a mix of crisis-driven displacement and pre-existing diaspora structures: shaping who relocates, where they relocate, and how they integrate.

### Why a Data-Driven Relocation Recommender is Needed

Sudanese individuals and families face complex decisions regarding relocation: weighing **safety, economic opportunity, family needs, visa access, community connection, and cost of living**, often under extreme pressure and uncertainty.  
These decisions are typically based on informal information: personal networks, social media, or anecdotal advice: rather than systematic, transparent, data-driven analysis.

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
| [Council on Foreign Relations: Conflict Tracker](https://www.cfr.org/global-conflict-tracker/conflict/power-struggle-sudan) | Overview of SAF–RSF power struggle and current conflict drivers |
| [UNHCR: Sudan Situation Dashboard](https://data.unhcr.org/en/situations/sudansituation)| Live displacement data, refugee flows, host countries |
| [UNHCR: Sudan Country Profile](https://data.unhcr.org/en/country/sdn) | Historical refugee context and internal displacement |
| [CMI: Sudanese Refugees in Saudi Arabia](https://www.cmi.no/publications/8834-saudi-arabia-and-sudanese-refugees) | Gulf migration, integration, identity and policy study |
| [ABC News: Humanitarian Nightmare Article](https://abcnews.go.com/International/sudan-now-worst-humanitarian-nightmares-recent-history/story?id=104173197) | Qualitative severity of humanitarian crisis |
| [IOM DTM: Visual Displacement Dashboard](https://dtm.iom.int/online-interactive-resources/one-year-conflict-sudan-visualizing-worlds-largest-displacement-crisis) | Internal displacement, border movements, data visualization |
| [Human Rights Watch: Darfur Report](https://www.hrw.org/reports/2007/sudan0907/sudan0907webtext.pdf) | Evidence of pre-2023 mass displacement |
  
### Why Relocation Recommendation Matters

- Many potential migrants have limited information about which destinations might offer the best balance of **safety**, **employment prospects**, **community support**, **cost of living**, and **social integration**.  
- A data-driven recommender can help reduce uncertainty. By combining individual preferences/constraints with objective indicators, it offers more informed, personalized relocation suggestions.  
- For displaced populations and humanitarian actors, such a tool could support better decision-making, planning, and support services: ensuring relocations are safer, more sustainable, and aligned with individual needs.

---

## Objectives & Research Questions

### Project Goal

The primary goal of this project is to develop a **machine-learning powered recommendation system** that supports Sudanese individuals and families in making informed decisions about relocation during and after the 2023–present crisis. By combining combined personal survey data with country-level socioeconomic indicators, the system will generate **ranked, interpretable suggestions** for potential relocation destinations.

### Core Objectives

1. **Collect and formalize individual-level preferences and constraints**  
   through a structured survey instrument targeting Sudanese respondents, including demographics, motivations, safety priorities, economic needs, family considerations, and legal/visa status.

2. **Integrate external, country-level and city-level feature data**  
   such as safety/security indexes, cost of living, diaspora presence, employment environments, education access, and immigration feasibility, to build a dataset useful for real-world relocation decisions.

3. **Develop a transparent recommendation algorithm**  
   capable of ranking destination countries (and potentially cities) based on multi-criteria decision logic, including both quantitative scoring and interpretable ML models.

4. **Generate human-readable output explanations**  
   that clearly communicate *why* a destination is recommended, highlighting the most important contributing features.

5. **Ensure ethical, fair, and responsible treatment of data**  
   especially regarding vulnerable populations, migration decision-making, representation bias, and privacy considerations.

---

### Research Questions

1. **Which factors most strongly influence relocation suitability for Sudanese migrants?**  
   Are safety concerns, cost of living, diaspora presence, or immigration feasibility the dominant drivers?

2. **How can quantitative and qualitative features be combined into a single ranking or scoring mechanism?**  
   What weighting strategies or normalization techniques make rankings fair and transparent?

3. **What machine-learning or rule-based frameworks perform best for relocation recommendations?**  
   (e.g., weighted multi-criteria scoring, clustering-based matching, hybrid ML + rule systems)

4. **Can we reliably recommend destinations using survey data from a limited number of respondents?**  
   What generalizations or pattern-matching techniques can make the system robust with small samples?

5. **How do pre-existing diaspora patterns and social networks influence choice and outcomes?**  
   Can community presence data improve recommendation accuracy and user confidence?

6. **How do legal and administrative constraints integrate into technical decision systems?**  
   Particularly visa availability, passport validity, residency pathways, and humanitarian corridors.

---

### Hypothesis (Working Assumption)

Relocation recommendations **improve in usefulness and trust** when:

- **Personal constraints** (family, budget, safety needs)  
are combined with  
- **Objective destination features** (cost of living, security, diaspora size, immigration pathways)  

We hypothesize that a **hybrid model**: using both rule-based filtering and machine-learning ranking — will produce recommendations that are both **interpretable and personalized**, outperforming purely ML or purely heuristic approaches.

---

### Expected Outcomes

- A reproducible **dataset** combining survey responses with destination indicators.
- A functioning **recommender prototype** (e.g., Streamlit or CLI tool).
- A baseline **ranking algorithm** + interpretability layer.
- Documentation describing limitations, assumptions, and ethical constraints.

---

## Data Collection & Survey Design

## Data Collection and Survey Design

This project uses a structured survey to collect individual level information from Sudanese respondents inside and outside Sudan. The survey gathers demographic, educational, financial, logistical, and preference based data to support relocation decision modeling. All data is collected anonymously through a Google Forms questionnaire.

Survey questions were designed to capture both personal constraints and target destination preferences. The responses are later combined with country level indicators to generate relocation recommendations.

Below is a high level breakdown of the survey categories and their intended modeling purpose.

---

### Survey Categories and Feature Rationale

| Category | Questions Covered | Why This Matters |
|--------|------------------|-----------------|
| **Demographics** | Age group, gender | Helps segment users into profiles. Supports demographic specific recommendations and trend analysis. |
| **Current Location and Motivation** | Current country, reason for living there | Identifies displacement patterns and migration history. Useful for modeling proximity, border dynamics, and expected migration flows. |
| **Family Status and Dependents** | Marital status, number of dependents | Family size affects budget needs, schooling, housing, medical support, and service requirements. |
| **Education Level and Professional Background** | Highest education, field of study, employment status, remote work possibility, years of experience | Determines employment potential, market matching, income expectations, and digital mobility. |
| **Language Skills** | Languages spoken | Language compatibility is a major relocation success factor and often determines integration speed. |
| **Relocation Intent and Objectives** | Are you seeking to relocate, goals for relocation | Separates active relocation planners from undecided respondents. Helps score urgency and priority features. |
| **Financial Capacity** | Monthly budget, ability to pay for visa and relocation fees | Budget constraints guide realistic destination filtering and cost of living scoring. |
| **Preferred Regions and Cultural Preferences** | Regional preference, cultural alignment | Allows weighted recommendations that respect cultural, linguistic, and regional familiarity. |
| **Travel and Legal Documentation** | Passport status, visa restrictions | Hard constraints that restrict which destination countries can be recommended. |
| **Support Needs and Special Requirements** | Support services required, medical or special needs | Integrates humanitarian considerations and can prioritize safe destinations with relevant support infrastructure. |

---

### Data Handling and Processing Approach

1. **Encoding**  
   Each multiple choice answer will be converted into numerical or categorical variables. Multi-select responses will be one hot encoded.

2. **Missing Data**  
   Responses with missing mandatory questions will be removed or imputed depending on type and significance.

3. **Feature Engineering**  
   - Budget ranges can be converted into numeric estimates.  
   - Regional preferences can be matched to country clusters.  
   - Visa and passport information can create eligibility filters.  
   - Dependents can be modeled as a weighting factor on cost of living and support services.

4. **External Data Integration**  
   The survey dataset will be combined with external country based indicators such as:
   - Cost of living indexes  
   - Safety and conflict risk assessments  
   - Diaspora population presence  
   - Employment opportunities  
   - Immigration policy and visa pathways  

5. **Privacy and Ethics**  
   No personal identifiers are collected. Survey data will be anonymized before storage. Sensitive attributes are handled with special care to avoid discriminatory model outputs.

---

### Data Structure in the Repository

Survey data will be exported as `.csv` and organized in:

```text
data/
raw/
survey_responses_original.csv
intermediate/
cleaned_responses.csv
processed/
final_model_dataset.csv
```

A detailed data dictionary and feature mapping will be added in `docs/variable_dictionary.md`.

---

## Data Pipeline & Methodology

1. **Data cleaning & preprocessing**: Remove invalid entries, encode categorical responses, handle missing data.  
2. **Feature engineering**: Combine survey responses + external country/city data to build a unified feature matrix for each candidate relocation destination per user profile.  
3. **Modeling / Recommendation logic**: Experiment with one or more of:  
   - Ranking algorithms (e.g. weighted-scoring, multi-criteria decision analysis),  
   - Clustering (to segment users and match to country clusters),  
   - Hybrid ML + rule-based system that balances quantitative and qualitative factors.  
4. **Evaluation**: Since “ground-truth” labels are hard, evaluation will be partly qualitative: simulate user-profiles and assess whether recommendations make sense; get feedback from peers / domain experts.  
5. **Deployment / Inference**: Build a simple interface (e.g. a web app or command-line tool) to capture user inputs and output recommended destinations + explanation.  

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

## Recommendation Logic and Modelling Approach

The relocation recommender will follow a hybrid approach that combines:

1. Rule based filtering using hard constraints  
2. Unsupervised clustering to understand patterns among users and countries  
3. Supervised learning with a neural network model to score user destination pairs  
4. K fold cross validation for robust evaluation and model selection  

This design keeps the system interpretable while allowing for more advanced machine learning components where they make sense.

---

### Step 1. Rule Based Eligibility Filter

Before any scoring or ranking, the system applies a hard filter that removes destinations that are clearly infeasible for a given user. Examples of hard constraints include:

- No valid passport and destination requires a visa that cannot be obtained  
- Monthly budget is significantly lower than the minimum estimated cost of living  
- Visa preference is "easy visa required" but destination has very restrictive entry conditions  
- User requires medical or special needs support and the destination has extremely low healthcare access ratings  

Only destinations that pass these constraints move on to the scoring and recommendation stages. This prevents unrealistic suggestions from appearing at the top of the list.

---

### Step 2. Unsupervised Clustering

Clustering is used in two complementary ways.

#### 2.1 Clustering respondents

Using features such as age group, education level, employment status, budget band, dependents, and preferred regions, respondents are grouped into clusters that represent common relocation profiles, for example:

- Young, single, remote capable professionals with moderate budgets  
- Families with children and low to medium budgets seeking safety and schooling  
- Highly educated individuals targeting further studies or scholarships  

Algorithms such as k means or hierarchical clustering can be used. These clusters are useful to:

- Understand typical user segments  
- Compare how different profiles map to different recommended destinations  
- Possibly calibrate different weighting schemes per cluster  

#### 2.2 Clustering destinations

Destination countries can also be clustered based on country feature schema, for example:

- Safety index  
- Cost of living index  
- Diaspora presence  
- Visa and immigration accessibility  
- Language and cultural compatibility  

This groups countries into profiles such as "high cost, high opportunity, high safety" or "low cost, nearer, moderate safety." For a given user cluster, the system can learn which destination clusters are more suitable.

---

### Step 3. Supervised Learning with a Neural Network

To move beyond fixed weights, the project will include a simple feed forward neural network that learns to predict a suitability score for a given (user, destination) pair.

#### 3.1 Input representation

For each user destination pair, we create a combined feature vector that includes:

- Encoded user features (from the survey variable dictionary)  
- Encoded destination features (from the country feature schema)  
- Interaction features where useful, for example budget compared to cost of living, language match flags, region preference match  

This vector is fed into the neural network.

#### 3.2 Labels and training strategy

Because there is no ground truth "best destination" label, the model will use proxy labels derived from the survey and heuristics, for example:

- Positive examples where the destination region matches the user preferred region and satisfies key constraints  
- Higher labels for countries that are known common choices for similar profiles (based on existing migration patterns)  
- Possibly user self reported "top choice" destinations, if added in future versions of the survey  

The neural network then learns to assign higher scores to destinations that align with user preferences and feasibility, compared to random alternatives.

#### 3.3 Network architecture (initial version)

A reasonable starting architecture is:

- Input layer: concatenated user and destination feature vector  
- One or two hidden layers with ReLU activations and dropout for regularization  
- Output layer: single neuron with linear or sigmoid activation representing a suitability score  

This keeps the model simple and interpretable enough for a relatively small dataset.

---

### Step 4. K Fold Cross Validation

To evaluate and tune the supervised component, k fold cross validation will be used.

1. The dataset of labeled user destination pairs is split into k folds.  
2. For each fold, the neural network is trained on k minus 1 folds and evaluated on the held out fold.  
3. Metrics such as ranking quality (for example mean reciprocal rank, top k accuracy, or pairwise accuracy) are computed.  
4. Results across folds are averaged to obtain a more stable estimate of performance.  

Cross validation also helps in:

- Selecting hyper-parameters such as learning rate, number of hidden units, and regularization strength  
- Comparing the neural network against simpler baselines such as pure weighted scoring or logistic regression  

---

### Step 5. Final Recommendation and Explanation

At inference time, the system will combine:

1. A rules based eligibility filter  
2. A baseline weighted score that uses transparent weights on safety, cost, diaspora, and preferences  
3. The neural network predicted suitability score  

A simple way to combine them is to compute a final score such as:

```text
final_score = alpha * baseline_score + (1 - alpha) * nn_score
```

Where alpha is a tunable parameter between 0 and 1.

For each recommended destination, the system will generate a short explanation such as:

"Recommended because it matches your Gulf region preference, has a significant Sudanese community, and fits your monthly budget."

"Recommended because you speak English, you are remote work capable, and this country has strong internet infrastructure and remote work opportunities."

These explanations will be derived from the most influential features for the baseline score and, where possible, feature importance approximations from the trained model.

---

## Getting Started

For instructions on running the recommender system via CLI or Streamlit, see:
➡️ [HOW_TO_USE.md](docs/HOW_TO_USE.md)

---

## Limitations and Ethics

This project works with sensitive humanitarian data and aims to support decision making for people affected by conflict and displacement. It is important to clearly state what the system can and cannot do.

### 1. No model can guarantee a successful relocation

The recommender system provides suggestions, not outcomes. Even if a country scores well on safety, cost of living, or cultural compatibility, relocation success depends on many external factors:

- Real visa decisions
- Individual circumstances
- Employment availability at the time of arrival
- Housing availability
- Social inclusion and legal treatment of foreign nationals

Users should view recommendations as informational guidance rather than definitive advice.

### 2. Data availability and quality limitations

The survey dataset may not be representative of all Sudanese populations. Internet access, safety conditions, and literacy affect who is able to respond. This may introduce sampling bias. Country level data is also approximate and may change rapidly due to political or economic developments.

### 3. Ethical handling of sensitive attributes

The model uses variables such as passport status, medical needs, and budget limitations. These are sensitive attributes and require responsible handling. No personally identifying information is collected. Data is anonymized and stored in structured form for analysis only.

### 4. Partial and proxy labeling for supervised learning

There is no ground truth dataset that defines a universally "best" relocation destination. Labels used in supervised learning come from proxy sources such as:

- Region preference match
- Budget and visa feasibility
- Known migration patterns

These can introduce bias because they reflect past decisions and constraints, not necessarily ideal options.

### 5. Risk of algorithmic bias

Models may favor destinations with more available data or countries with historically large diaspora communities. Smaller countries or regions with limited data may be underrepresented. Clustering and learned weights may unintentionally push respondents toward common or familiar destinations.

Mitigation strategies include:

- Human review for unusual recommendations
- Balanced representation of destination groups
- Regular review of feature importance and model outputs

### 6. Changing humanitarian conditions

Safety, immigration policies, and economic conditions can change rapidly, especially during conflict. Model outputs become outdated if country level data is not refreshed regularly. Users should be aware that recommendations reflect information at a specific point in time.

### 7. Human responsibility and agency

A recommendation system should never replace personal judgment or professional guidance from humanitarian organizations, legal experts, or community support groups. The goal is to provide structured information to support, not replace, human decision making.

### 8. Transparency and documentation

All assumptions, scoring rules, and features are documented openly in this repository. Future revisions will include:

- Versioning of country feature datasets
- Change logs for model updates
- Clear labeling of proxy indicators used for training

Transparency helps reduce misinterpretation and allows community feedback.

### 9. Ethical review for deployment

When moving from project prototype to real world use, additional steps are recommended:

- Consult with humanitarian actors or NGOs
- Review ethical considerations with regional experts
- Ensure compliance with local and international data protection standards

This is especially important when working with displaced populations or vulnerable individuals at risk of exploitation or discrimination.

---
*Disclaimer: This project is intended for research and educational purposes as part of the MIT Emerging Talent program. Recommendations generated by this system should not be interpreted as legal, migration, or humanitarian advice.*
