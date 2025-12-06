"""
Streamlit app for the Sudanese Relocation Recommender.

Run from project root with:

    streamlit run app.py
"""

from __future__ import annotations

from pathlib import Path
from typing import List

import pandas as pd
import streamlit as st

from src.recommendation.recommender import (
    load_country_features,
    load_model_and_scaler,
    recommend_destinations,
)


def get_project_paths() -> dict:
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


def main():
    st.set_page_config(page_title="Sudanese Relocation Recommender", layout="wide")

    st.title("Sudanese Relocation Recommender")
    st.write(
        "An experimental recommendation system to explore relocation options "
        "for Sudanese individuals, based on survey responses and country features."
    )

    paths = get_project_paths()
    processed_dir = paths["processed_dir"]
    intermediate_dir = paths["intermediate_dir"]
    model_dir = paths["model_dir"]
    external_dir = paths["external_dir"]

    # Load data
    user_file_with_clusters = processed_dir / "final_model_dataset_with_clusters.csv"
    user_file_basic = processed_dir / "final_model_dataset.csv"

    if user_file_with_clusters.exists():
        user_df = pd.read_csv(user_file_with_clusters)
        user_source = user_file_with_clusters.name
    else:
        user_df = pd.read_csv(user_file_basic)
        user_source = user_file_basic.name

    raw_clean_file = intermediate_dir / "cleaned_responses.csv"
    if raw_clean_file.exists():
        raw_users_df = pd.read_csv(raw_clean_file)
    else:
        raw_users_df = None

    country_df = load_country_features(external_dir / "country_features.csv")
    scaler, nn_model = load_model_and_scaler(model_dir)

    user_feature_cols = infer_user_feature_cols(user_df)
    country_feature_cols = infer_country_feature_cols(country_df)

    st.sidebar.header("Configuration")
    st.sidebar.write(f"User dataset: `{user_source}`")

    # Select user by index
    user_index = st.sidebar.number_input(
        "User index", min_value=0, max_value=len(user_df) - 1, value=0, step=1
    )

    top_k = st.sidebar.slider("Top K recommendations", min_value=3, max_value=10, value=5, step=1)
    alpha = st.sidebar.slider(
        "Baseline vs Neural Network weight (α)",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.05,
        help="final_score = α * baseline + (1 - α) * NN",
    )

    # Show user profile
    st.subheader("Selected user profile")

    user_row = user_df.iloc[user_index]

    if raw_users_df is not None and len(raw_users_df) == len(user_df):
        # Show raw survey fields if available
        cols_to_show = [
            col
            for col in [
                "age_group",
                "gender",
                "current_country",
                "relocation_intent",
                "budget_band",
                "preferred_regions",
            ]
            if col in raw_users_df.columns
        ]
        st.write("**Survey answers:**")
        st.table(raw_users_df[cols_to_show].iloc[[user_index]])
    else:
        # Fallback to engineered features
        cols_to_show = [
            c
            for c in [
                "age_group_ord",
                "budget_estimated_usd",
                "remote_capable",
                "actively_seeking",
            ]
            if c in user_df.columns
        ]
        st.write("**Feature-based view:**")
        st.table(user_df[cols_to_show].iloc[[user_index]])

    st.write("**Model features used for this user:**")
    st.code(", ".join(user_feature_cols))

    # Compute recommendations
    if st.button("Generate recommendations"):
        with st.spinner("Computing recommendations..."):
            recs = recommend_destinations(
                user_features=user_row,
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
            recs[["country_name", "country_code", "final_score", "nn_score", "baseline_score", "explanation"]],
            use_container_width=True,
        )

        st.caption(
            "Note: Scores are relative; higher final_score means a stronger recommended match. "
            "The final_score blends a transparent heuristic with a learned neural network model."
        )


if __name__ == "__main__":
    main()
