# Destination Country Feature Schema

In addition to individual survey data, this project relies on external indicators that describe each potential destination country or region. These features are used to score and rank destinations based on safety, cost of living, integration potential, and feasibility.

Below is a proposed schema for destination level features.

## 1. Identification and Basic Info

| Feature Name | Type | Description | Example Source |
|--------------|------|-------------|----------------|
| `country_code` | Categorical (string) | ISO country code or custom identifier. | ISO standards |
| `country_name` | Categorical (string) | Full country name. | ISO / manual |
| `region_group` | Categorical | Region category such as gulf, east_africa, north_africa, europe, uk_ireland, north_america, asia. | Manual mapping |

## 2. Safety and Stability

| Feature Name | Type | Description | Example Source |
|--------------|------|-------------|----------------|
| `safety_index` | Numeric | Composite safety or security score. Higher can mean safer, depending on the index. | Global peace index, travel advisory summaries |
| `conflict_risk_level` | Categorical / ordinal | Rough classification such as low, medium, high conflict risk. | Humanitarian or security reports |
| `political_stability_score` | Numeric | Governance or stability score where available. | Worldwide governance indicators |

## 3. Economic and Employment Indicators

| Feature Name | Type | Description | Example Source |
|--------------|------|-------------|----------------|
| `gdp_per_capita` | Numeric | GDP per capita (USD) as a proxy for economic development. | World Bank |
| `unemployment_rate` | Numeric | General unemployment rate. | National statistics / World Bank |
| `employment_opportunity_score` | Numeric (0–1 or 0–100) | Derived or composite score reflecting job prospects for migrants in general or Sudanese profiles in particular. | Constructed metric |
| `demand_for_remote_work` | Numeric / categorical | Indicator of how friendly the country is to remote / online work (infrastructure, platforms, regulatory environment). | Constructed metric |

## 4. Cost of Living and Affordability

| Feature Name | Type | Description | Example Source |
|--------------|------|-------------|----------------|
| `cost_of_living_index` | Numeric | General cost of living index relative to a baseline city or global average. | Numbeo or similar |
| `rent_index` | Numeric | Cost of housing index. | Cost of living datasets |
| `healthcare_cost_level` | Categorical / numeric | Approximate relative cost of medical care. | Healthcare stats, cost of living reports |
| `education_cost_level` | Categorical / numeric | Approximate cost for schooling or higher education. | Education reports |

These features will later be compared against the respondent’s monthly budget and family size.

## 5. Legal and Immigration Feasibility

| Feature Name | Type | Description | Example Source |
|--------------|------|-------------|----------------|
| `visa_policy_sudanese` | Categorical | Broad category such as visa_free, visa_on_arrival, e_visa, embassy_visa, very_restrictive for Sudanese passport holders. | Immigration policy summaries, consular info |
| `average_visa_processing_difficulty` | Ordinal | Simple score such as 1 (easy) to 5 (very difficult) based on processing time, documentation burden, and rejection rates. | Constructed metric |
| `work_permit_accessibility` | Ordinal | Score of how accessible legal work permits are for foreign nationals. | Migration policy databases |
| `humanitarian_pathways_available` | Binary / categorical | Indicates presence of asylum / humanitarian visa routes that Sudanese may use. | UNHCR, national asylum systems |

These map directly to survey features like `visa_preference`, `passport_status`, and `can_pay_visa`.

## 6. Social Integration and Community

| Feature Name | Type | Description | Example Source |
|--------------|------|-------------|----------------|
| `sudanese_diaspora_size` | Numeric | Estimated number of Sudanese nationals residing in the country. | UN, IOM, diaspora estimates |
| `diaspora_presence_score` | Numeric | Normalized score for diaspora presence, for example 0–1 based on size per population. | Constructed metric |
| `arabic_language_official` | Binary | 1 if Arabic is official or widely spoken, 0 otherwise. | Language databases |
| `english_language_widely_spoken` | Binary | 1 if English use is high in urban and work environments. | Language stats |
| `cultural_compatibility_score` | Numeric | Approximate compatibility with cultural preference such as arabic_speaking, african, western. | Constructed mapping based on region and language |

These features pair with survey responses on languages, cultural preferences, and support needs.

## 7. Services and Support Infrastructure

| Feature Name | Type | Description | Example Source |
|--------------|------|-------------|----------------|
| `access_to_public_healthcare` | Ordinal | Rough rating of accessibility and quality of public health services. | WHO, national health stats |
| `refugee_support_programs` | Binary / categorical | Indicates presence of formal refugee support or integration programs. | UNHCR, NGO reports |
| `education_access_refugees` | Ordinal | Rating for how accessible schooling and higher education are for refugees or migrants. | Education and refugee reports |
| `housing_support_availability` | Ordinal | Rating for availability of affordable housing or housing assistance programs. | Local reports, humanitarian assessments |

These connect to the survey variable `support_needed` (job placement, housing, language training, scholarships, legal support, medical support, child education).

## 8. Geography and Proximity

| Feature Name | Type | Description | Example Source |
|--------------|------|-------------|----------------|
| `distance_from_sudan_km` | Numeric | Approximate distance from Sudan to main destination city or capital, in kilometers. | Geospatial calculations |
| `bordering_sudan` | Binary | 1 if country shares a land border with Sudan, 0 otherwise. | Geographic data |
| `climate_similarity_score` | Numeric | Approximate similarity of climate to Sudan, used for comfort or adaptation modeling. | Climate data |

---

## How These Features Will Be Used

1. **Filtering step**  
   Hard constraints such as passport status, visa feasibility, and budget will be used to filter out destinations that are clearly infeasible.

2. **Scoring step**  
   Remaining countries will be scored using a weighted combination of:
   - Safety and stability  
   - Cost of living and affordability  
   - Employment and economic opportunity  
   - Cultural and language compatibility  
   - Diaspora and support availability  

3. **Ranking step**  
   Destinations are ranked for each respondent, with the top results forming the recommendation list.

4. **Explanation step**  
   The recommender will surface the top factors for each suggested country. For example:  
   - “This country matches your Arabic language preference and has a large Sudanese community.”  
   - “This destination offers relatively lower cost of living given your budget and has accessible humanitarian pathways.”
