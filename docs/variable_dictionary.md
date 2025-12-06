# Variable Dictionary (Survey Features)

This table describes how each survey question is transformed into model features.

## 1. Demographics

| Q# | Original Question | Feature Name(s) | Type | Encoding / Notes |
|----|-------------------|-----------------|------|------------------|
| 1 | Age Group | `age_group` | Categorical (ordinal) | Map categories to ordered integers, for example: 18_24 = 1, 25_34 = 2, 35_44 = 3, 45_54 = 4, 55_plus = 5. |
| 2 | Gender | `gender` | Categorical | One hot encode (male, female, prefer_not_say) or keep as single categorical. |

## 2. Current Location and Reason

| Q# | Original Question | Feature Name(s) | Type | Encoding / Notes |
|----|-------------------|-----------------|------|------------------|
| 3 | Current Location | `current_country` | Categorical | Values like sudan, egypt, saudi_arabia, uae, qatar, turkey, kenya, other. Consider a separate flag `current_country_other`. |
| 4 | Reason for Current Country of Residence | `reason_current_country` | Categorical | One hot encode categories such as safety, employment, education, family_reunion, pre_war_resident, medical, transit, other. |

## 3. Family Status and Dependents

| Q# | Original Question | Feature Name(s) | Type | Encoding / Notes |
|----|-------------------|-----------------|------|------------------|
| 5 | Marital Status | `marital_status` | Categorical | Categories: single, married_no_children, married_with_children. Can also create binary flags like `has_children`. |
| 6 | Number of Dependents / Family Members Moving | `dependents_category`, `dependents_estimated` | Categorical + Numeric | Keep the chosen band as categorical (0, 1, 2, 3_4, 5_plus). Optionally map to an approximate number (0, 1, 2, 3.5, 5) for cost calculations. |

## 4. Education and Profession

| Q# | Original Question | Feature Name(s) | Type | Encoding / Notes |
|----|-------------------|-----------------|------|------------------|
| 7 | Highest Level of Education | `education_level` | Categorical (ordinal) | Order levels from no_formal_education up to phd. This can be encoded as an integer scale for modeling. |
| 8 | Field of Study | `field_engineering`, `field_healthcare`, `field_business`, `field_education`, `field_it`, `field_law`, `field_other` | Multi-label (binary flags) | Multi select. Create one binary feature per field. `field_other` can indicate other disciplines. |
| 9 | Current Employment Status | `employment_status` | Categorical | Categories: employed_full_time, employed_part_time, self_employed, unemployed_looking, unemployed_not_looking, student, retired. One hot encode. |
| 10 | Years of Professional Experience | `experience_years_band`, `experience_years_estimated` | Categorical + Numeric | Use band as categorical (0_1, 2_4, 5_7, 8_10, 10_plus). Optionally map to an approximate number (0.5, 3, 6, 9, 12). |
| 11 | Ability to Work Remotely | `remote_capable` | Binary | Map to binary flag. For example: 1 if respondent has laptop and can work remotely, 0 if depends on local physical work. |

## 5. Languages

| Q# | Original Question | Feature Name(s) | Type | Encoding / Notes |
|----|-------------------|-----------------|------|------------------|
| 12 | What languages do you speak | `lang_arabic`, `lang_english`, `lang_french`, `lang_german`, `lang_italian`, `lang_spanish`, `lang_other` | Multi-label (binary flags) | Multi select. Create binary flag for each language. `lang_other` can capture additional languages. These can later be matched to destination language requirements. |

## 6. Relocation Intent and Goals

| Q# | Original Question | Feature Name(s) | Type | Encoding / Notes |
|----|-------------------|-----------------|------|------------------|
| 13 | Are you seeking to relocate | `relocation_intent` | Categorical | Values: yes, no, not_sure. You can also create a binary `actively_seeking` flag that is 1 for yes only. |
| 14 | Main goal for relocation | `relocation_goal` | Categorical | Categories such as employment, education, safety, healthcare, family_reunification, business, temporary_until_return, permanent_settlement, not_seeking, other. One hot encode these. |

## 7. Financial and Logistical Constraints

| Q# | Original Question | Feature Name(s) | Type | Encoding / Notes |
|----|-------------------|-----------------|------|------------------|
| 15 | Monthly Budget for Living Expenses (USD) | `budget_band`, `budget_estimated_usd` | Categorical + Numeric | Keep band as categorical. Also map to midpoints, for example: `<200` = 150, `200_500` = 350, `500_1000` = 750, `1000_2500` = 1750, `2500_5000` = 3750, `>5000` = 6000. |
| 16 | Ability to pay for relocation / visa fees | `can_pay_visa` | Categorical or ordinal | Values: yes, partially, no. Could be mapped to scores (2, 1, 0) to approximate financial flexibility. |

## 8. Preferences and Cultural Alignment

| Q# | Original Question | Feature Name(s) | Type | Encoding / Notes |
|----|-------------------|-----------------|------|------------------|
| 17 | Preferred Regions for Relocation | `pref_gulf`, `pref_east_africa`, `pref_north_africa`, `pref_europe`, `pref_uk_ireland`, `pref_canada`, `pref_usa`, `pref_asia`, `pref_anywhere` | Multi-label (binary flags) | Multi select. Create one binary feature per region. These can be used as positive weights when scoring destinations. |
| 18 | Cultural Preferences | `cultural_preference` | Categorical | Categories: arabic_speaking, african, western, no_preference. This can be used as a multiplier for destinations that match the cultural group. |

## 9. Documentation and Legal Constraints

| Q# | Original Question | Feature Name(s) | Type | Encoding / Notes |
|----|-------------------|-----------------|------|------------------|
| 19 | Do you currently have a passport | `passport_status` | Categorical | Categories: valid, expired, expiring_soon, no_passport, in_process. These inform feasibility and urgency. |
| 20 | Visa Restrictions | `visa_preference` | Categorical | Categories: easy_visa_required, willing_long_process, sponsorship_only. This can filter or low weight destinations with very restrictive regimes. |

## 10. Support Needs and Special Requirements

| Q# | Original Question | Feature Name(s) | Type | Encoding / Notes |
|----|-------------------|-----------------|------|------------------|
| 21 | Support Needed | `need_job`, `need_housing`, `need_language_training`, `need_scholarship`, `need_legal_support`, `need_child_education`, `need_medical_support`, `need_none` | Categorical or multi-label | The question is single choice in the current design, so keep `support_needed` as a categorical field or explode into binary flags if you later allow multi select. |
| 22 | Medical or special needs to consider | `special_needs` | Categorical / Binary | Values: yes, no, prefer_not_to_say. You can map `yes` to a binary flag and handle it with extra care and privacy. |

---
