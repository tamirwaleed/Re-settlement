"""
Streamlit app for the Sudanese Relocation Recommender.

Run from project root with:

    python -m streamlit run app.py
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Dict, Any

import pandas as pd
import streamlit as st

from src.recommendation.recommender import (
    load_country_features,
    load_model_and_scaler,
    recommend_destinations,
)


def get_project_paths() -> Dict[str, Path]:
    this_file = Path(__file__).resolve()
    project_root = this_file.parent
    notebooks_dir = project_root / "notebooks"
    processed_dir = notebooks_dir / "processed"
    intermediate_dir = notebooks_dir / "intermediate"
    model_dir = processed_dir / "models"
    external_dir = project_root / "data" / "external"

    return {
        "project_root": project_root,
        "notebooks_dir": notebooks_dir,
        "processed_dir": processed_dir,
        "intermediate_dir": intermediate_dir,
        "model_dir": model_dir,
        "external_dir": external_dir,
    }


def infer_user_feature_cols(user_df: pd.DataFrame) -> List[str]:
    """
    Infer the feature columns that the model expects for users.
    """
    candidates = [
        "age_group_ord",
        "dependents_estimated",
        "experience_years_est",
        "budget_estimated_usd",
        "remote_capable",
        "actively_seeking",
        "pref_gulf",
        "pref_east_africa",
        "pref_north_africa",
        "pref_europe",
        "pref_uk_ireland",
        "pref_canada",
        "pref_usa",
        "pref_asia",
        "pref_anywhere",
    ]
    return [c for c in candidates if c in user_df.columns]


def infer_country_feature_cols(country_df: pd.DataFrame) -> List[str]:
    """
    Infer the feature columns that the model expects for countries.
    """
    candidates = [
        "country_code",
        "safety_index",
        "cost_of_living_index",
        "diaspora_presence_score",
        "visa_policy_sudanese_score",
        "cultural_compatibility_score",
        "min_budget_required",
    ]
    return [c for c in candidates if c in country_df.columns]


def encode_age_group(age_label: str) -> int:
    mapping = {
        "18-24": 0,
        "25-34": 1,
        "35-44": 2,
        "45-54": 3,
        "55+": 4,
    }
    return mapping.get(age_label, 1)


def build_user_from_form(
    age_group: str,
    monthly_budget: float,
    remote_choice: str,
    region_prefs: List[str],
    wants_to_relocate: bool,
    speaks_english: bool,
    cultural_pref: str,
) -> Dict[str, Any]:
    """
    Build a user feature dictionary that matches the model expectations
    as closely as possible using the form inputs.
    """
    age_group_ord = encode_age_group(age_group)

    # Basic flags
    remote_capable = 1 if "remote" in remote_choice.lower() else 0
    actively_seeking = 1 if wants_to_relocate else 0

    # Region preferences mapping
    pref_gulf = 1 if "Gulf countries (UAE, Saudi, Qatar)" in region_prefs else 0
    pref_east_africa = 1 if "East Africa (Kenya, Ethiopia, Uganda)" in region_prefs else 0
    pref_north_africa = 1 if "North Africa (Egypt, Libya, Tunisia)" in region_prefs else 0
    pref_europe = 1 if "Europe" in region_prefs else 0
    pref_uk_ireland = 1 if "UK / Ireland" in region_prefs else 0
    pref_canada = 1 if "Canada" in region_prefs else 0
    pref_usa = 1 if "USA" in region_prefs else 0
    pref_asia = 1 if "Asia (Malaysia, China)" in region_prefs else 0
    pref_anywhere = 1 if "Anywhere / No preference" in region_prefs else 0

    # Some fields are used only for explanations, not necessarily in the model
    cultural_preference = cultural_pref
    lang_english = 1 if speaks_english else 0

    # Defaults for features we are not explicitly asking about
    dependents_estimated = 0
    experience_years_est = 0

    user_features: Dict[str, Any] = {
        "age_group_ord": age_group_ord,
        "budget_estimated_usd": float(monthly_budget),
        "remote_capable": remote_capable,
        "actively_seeking": actively_seeking,
        "pref_gulf": pref_gulf,
        "pref_east_africa": pref_east_africa,
        "pref_north_africa": pref_north_africa,
        "pref_europe": pref_europe,
        "pref_uk_ireland": pref_uk_ireland,
        "pref_canada": pref_canada,
        "pref_usa": pref_usa,
        "pref_asia": pref_asia,
        "pref_anywhere": pref_anywhere,
        "dependents_estimated": dependents_estimated,
        "experience_years_est": experience_years_est,
        # Extra fields used by explanation function
        "cultural_preference": cultural_preference,
        "lang_english": lang_english,
    }

    return user_features


def main():
    st.set_page_config(page_title="Sudanese Relocation Recommender", layout="wide")

    st.title("Sudanese Relocation Recommender")
    st.write(
        "An experimental recommendation system to explore relocation options "
        "for Sudanese individuals based on simple profile inputs and country features."
    )

    paths = get_project_paths()
    processed_dir = paths["processed_dir"]
    model_dir = paths["model_dir"]
    external_dir = paths["external_dir"]

    # Load user dataset only to infer model feature columns
    user_file_with_clusters = processed_dir / "final_model_dataset_with_clusters.csv"
    user_file_basic = processed_dir / "final_model_dataset.csv"

    if user_file_with_clusters.exists():
        user_df = pd.read_csv(user_file_with_clusters)
        user_source = user_file_with_clusters.name
    else:
        user_df = pd.read_csv(user_file_basic)
        user_source = user_file_basic.name

    # Load country features and model
    country_df = load_country_features(external_dir / "country_features.csv")
    scaler, nn_model = load_model_and_scaler(model_dir)

    user_feature_cols = infer_user_feature_cols(user_df)
    country_feature_cols = infer_country_feature_cols(country_df)

    st.sidebar.header("Configuration")
    st.sidebar.write(f"Model trained on: `{user_source}`")

    top_k = st.sidebar.slider(
        "Top K recommendations",
        min_value=3,
        max_value=10,
        value=5,
        step=1,
    )
    alpha = st.sidebar.slider(
        "Baseline vs Neural Network weight (α)",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.05,
        help="final_score = α * baseline + (1 - α) * NN",
    )

    st.subheader("Enter your profile")

    col1, col2 = st.columns(2)

    with col1:
        age_group = st.selectbox(
            "Age group",
            ["18-24", "25-34", "35-44", "45-54", "55+"],
            index=1,
        )

        monthly_budget = st.number_input(
            "Estimated monthly budget for living expenses (USD)",
            min_value=50.0,
            max_value=10000.0,
            value=800.0,
            step=50.0,
        )

        remote_choice = st.selectbox(
            "Work type",
            [
                "I can work remotely / freelance",
                "I mainly rely on local/physical work",
            ],
        )

    with col2:
        region_prefs = st.multiselect(
            "Preferred regions (you can select multiple)",
            [
                "Gulf countries (UAE, Saudi, Qatar)",
                "East Africa (Kenya, Ethiopia, Uganda)",
                "North Africa (Egypt, Libya, Tunisia)",
                "Europe",
                "UK / Ireland",
                "Canada",
                "USA",
                "Asia (Malaysia, China)",
                "Anywhere / No preference",
            ],
            default=["Gulf countries (UAE, Saudi, Qatar)"],
        )

        wants_to_relocate = st.checkbox(
            "I am actively seeking to relocate",
            value=True,
        )

        speaks_english = st.checkbox(
            "I can communicate in English",
            value=True,
        )

        cultural_pref = st.selectbox(
            "Cultural preference",
            [
                "Prefer Arabic-speaking countries",
                "Prefer African countries",
                "Prefer Western countries",
                "No strong preference",
            ],
            index=0,
        )

    if st.button("Generate recommendations"):
        user_features = build_user_from_form(
            age_group=age_group,
            monthly_budget=monthly_budget,
            remote_choice=remote_choice,
            region_prefs=region_prefs,
            wants_to_relocate=wants_to_relocate,
            speaks_english=speaks_english,
            cultural_pref=cultural_pref,
        )

        st.markdown("### Encoded user features (for transparency)")
        st.json(user_features)

        with st.spinner("Computing recommendations..."):
            recs = recommend_destinations(
                user_features=user_features,
                country_df=country_df,
                user_feature_cols=user_feature_cols,
                country_feature_cols=country_feature_cols,
                scaler=scaler,
                nn_model=nn_model,
                top_k=top_k,
                alpha=alpha,
            )

        st.subheader("Top recommendations")
        st.dataframe(
            recs[
                [
                    "country_name",
                    "country_code",
                    "final_score",
                    "nn_score",
                    "baseline_score",
                    "explanation",
                ]
            ],
            use_container_width=True,
        )

        st.caption(
            "These suggestions are experimental and meant to support, not replace, careful human judgment."
        )


if __name__ == "__main__":
    main()
