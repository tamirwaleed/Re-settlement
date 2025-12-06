"""
CLI demo for the Sudanese Relocation Recommender.

Usage (from project root):

    python -m src.recommendation.cli_demo --user-index 0 --top-k 5 --alpha 0.5
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import List

import pandas as pd

from .recommender import (
    load_country_features,
    load_model_and_scaler,
    recommend_destinations,
)


def get_project_paths() -> dict:
    """
    Infer project structure based on this file's location.

    Expected layout:
        project_root/
          src/
            recommendation/
              cli_demo.py
              recommender.py
          notebooks/
            processed/
              final_model_dataset_with_clusters.csv
              final_model_dataset.csv
              models/
          data/
            external/
              country_features.csv
    """
    this_file = Path(__file__).resolve()
    project_root = this_file.parents[2]  # .../Re-settlement
    notebooks_dir = project_root / "notebooks"
    processed_dir = notebooks_dir / "processed"
    model_dir = processed_dir / "models"
    external_dir = project_root / "data" / "external"

    return {
        "project_root": project_root,
        "notebooks_dir": notebooks_dir,
        "processed_dir": processed_dir,
        "model_dir": model_dir,
        "external_dir": external_dir,
    }


def infer_user_feature_cols(user_df: pd.DataFrame) -> List[str]:
    """
    Select the user feature columns used in the NN model.
    Must match the training notebook.
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
    Select the country feature columns used in the NN model.
    Must match the training notebook.
    """
    candidates = [
        "country_code",  # id column
        "safety_index",
        "cost_of_living_index",
        "diaspora_presence_score",
        "visa_policy_sudanese_score",
        "cultural_compatibility_score",
        "min_budget_required",
    ]
    return [c for c in candidates if c in country_df.columns]


def main():
    paths = get_project_paths()
    processed_dir = paths["processed_dir"]
    model_dir = paths["model_dir"]
    external_dir = paths["external_dir"]

    # CLI arguments
    parser = argparse.ArgumentParser(description="Sudanese Relocation Recommender CLI demo")
    parser.add_argument(
        "--user-index",
        type=int,
        default=0,
        help="Index of the user row in final_model_dataset (default: 0)",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Number of destinations to recommend (default: 5)",
    )
    parser.add_argument(
        "--alpha",
        type=float,
        default=0.5,
        help="Weight between baseline and NN scores (0.0–1.0, default: 0.5)",
    )
    args = parser.parse_args()

    # Load user features
    user_file_with_clusters = processed_dir / "final_model_dataset_with_clusters.csv"
    user_file_basic = processed_dir / "final_model_dataset.csv"

    if user_file_with_clusters.exists():
        user_df = pd.read_csv(user_file_with_clusters)
        print(f"Loaded user dataset: {user_file_with_clusters}")
    else:
        user_df = pd.read_csv(user_file_basic)
        print(f"Loaded user dataset: {user_file_basic}")

    if args.user_index < 0 or args.user_index >= len(user_df):
        raise IndexError(f"user_index {args.user_index} out of range (0..{len(user_df)-1})")

    # Load countries
    country_file = external_dir / "country_features.csv"
    country_df = load_country_features(country_file)
    print(f"Loaded countries from: {country_file}")

    # Load model and scaler
    scaler, nn_model = load_model_and_scaler(model_dir)

    # Infer feature columns
    user_feature_cols = infer_user_feature_cols(user_df)
    country_feature_cols = infer_country_feature_cols(country_df)

    print("\nUsing user features:", user_feature_cols)
    print("Using country features:", country_feature_cols)

    # Pick user row
    user_row = user_df.iloc[args.user_index]

    # Print a short summary of the user (if columns exist)
    print(f"\n===== User {args.user_index} profile =====")
    summary_cols = [
        c for c in ["age_group_ord", "budget_estimated_usd", "remote_capable", "actively_seeking"]
        if c in user_df.columns
    ]
    print(user_row[summary_cols])

    # Get recommendations
    recs = recommend_destinations(
        user_features=user_row,
        country_df=country_df,
        user_feature_cols=user_feature_cols,
        country_feature_cols=country_feature_cols,
        scaler=scaler,
        nn_model=nn_model,
        top_k=args.top_k,
        alpha=args.alpha,
    )

    # Pretty print
    print(f"\n===== Top {args.top_k} destination recommendations =====")
    for i, row in recs.iterrows():
        print(f"\n[{i+1}] {row['country_name']} ({row['country_code']})")
        print(f"  final_score   : {row['final_score']:.3f}")
        print(f"  nn_score      : {row['nn_score']:.3f}")
        print(f"  baseline_score: {row['baseline_score']:.3f}")
        print(f"  explanation   : {row['explanation']}")


if __name__ == "__main__":
    main()
