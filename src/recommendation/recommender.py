"""
Recommender module for Sudanese relocation project.

This module provides:
- Loading of trained NN model and scaler
- Loading of country features
- Baseline heuristic scoring
- Combined NN + baseline scoring
- Simple explanation strings for each recommendation
- A main recommend_destinations(...) function
"""

from __future__ import annotations

from pathlib import Path
from typing import Sequence, Optional, Tuple, Union

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
import joblib


# --------------------------------------------------------------------------
# Paths and loading helpers
# --------------------------------------------------------------------------


def load_country_features(path: Union[str, Path]) -> pd.DataFrame:
    """
    Load destination country feature dataset.

    Parameters
    ----------
    path : str or Path
        Path to country_features.csv as defined in docs/country_features.md.

    Returns
    -------
    DataFrame
        Country features with one row per destination.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Could not find country_features file at {path}")
    return pd.read_csv(path)


def load_model_and_scaler(
    model_dir: Union[str, Path],
    scaler_name: str = "nn_scaler.joblib",
    model_name: str = "nn_model.joblib",
) -> Tuple[StandardScaler, MLPRegressor]:
    """
    Load trained StandardScaler and MLPRegressor model.

    Parameters
    ----------
    model_dir : str or Path
        Directory containing scaler and model joblib files.
    scaler_name : str
        File name of the scaler joblib.
    model_name : str
        File name of the model joblib.

    Returns
    -------
    scaler : StandardScaler
    model : MLPRegressor
    """
    model_dir = Path(model_dir)
    scaler_path = model_dir / scaler_name
    model_path = model_dir / model_name

    if not scaler_path.exists():
        raise FileNotFoundError(f"Scaler not found at {scaler_path}")
    if not model_path.exists():
        raise FileNotFoundError(f"Model not found at {model_path}")

    scaler = joblib.load(scaler_path)
    model = joblib.load(model_path)

    return scaler, model


# --------------------------------------------------------------------------
# Scoring helpers
# --------------------------------------------------------------------------


def baseline_proxy_score(user_row: pd.Series, country_row: pd.Series) -> float:
    """
    Compute a transparent heuristic suitability score for a (user, country) pair.
    Higher score means a better match.

    This should stay aligned with the README and modeling notebook.
    """
    score = 0.0

    # Safety
    safety = country_row.get("safety_index", np.nan)
    if not pd.isna(safety):
        score += 0.3 * float(safety)

    # Cost of living (lower is better)
    cost_index = country_row.get("cost_of_living_index", np.nan)
    budget = user_row.get("budget_estimated_usd", np.nan)
    min_budget = country_row.get("min_budget_required", np.nan)

    if not pd.isna(cost_index):
        score += 0.1 * (-float(cost_index))

    # Budget fit
    if not pd.isna(budget) and not pd.isna(min_budget):
        budget_val = float(budget)
        min_budget_val = float(min_budget)
        if budget_val >= min_budget_val:
            score += 0.15
        else:
            score -= 0.15

    # Diaspora presence
    diaspora = country_row.get("diaspora_presence_score", np.nan)
    if not pd.isna(diaspora):
        score += 0.2 * float(diaspora)

    # Cultural compatibility
    cultural = country_row.get("cultural_compatibility_score", np.nan)
    if not pd.isna(cultural):
        score += 0.1 * float(cultural)

    # Visa policy
    visa_score = country_row.get("visa_policy_sudanese_score", np.nan)
    if not pd.isna(visa_score):
        score += 0.1 * float(visa_score)

    return float(score)


def prepare_features_for_model(
    X_pairs_filled: pd.DataFrame, scaler: StandardScaler
) -> np.ndarray:
    """
    Align feature columns with what the scaler was trained on.

    - Adds missing columns (filled with 0)
    - Reorders columns to match scaler.feature_names_in_
    """
    train_cols = getattr(scaler, "feature_names_in_", None)

    # Very old sklearn may not have feature_names_in_
    if train_cols is None:
        return scaler.transform(X_pairs_filled)

    train_cols = list(train_cols)

    # Add missing columns as zeros
    for col in train_cols:
        if col not in X_pairs_filled.columns:
            X_pairs_filled[col] = 0

    # Keep only training columns, in same order
    X_aligned = X_pairs_filled[train_cols]

    return scaler.transform(X_aligned)


def generate_explanation(user_row: pd.Series, country_row: pd.Series) -> str:
    """
    Basic human readable explanation for a recommended destination.
    Uses a few simple rules based on region, budget, culture, diaspora, safety.
    """
    parts: list[str] = []

    region_group = country_row.get("region_group", "")
    budget = user_row.get("budget_estimated_usd", None)
    min_budget = country_row.get("min_budget_required", None)

    # Region preferences flags (optional user features)
    if region_group == "gulf" and user_row.get("pref_gulf", 0) == 1:
        parts.append("matches your preference for Gulf countries")
    if region_group == "east_africa" and user_row.get("pref_east_africa", 0) == 1:
        parts.append("matches your preference for East Africa")
    if region_group == "north_africa" and user_row.get("pref_north_africa", 0) == 1:
        parts.append("matches your preference for North Africa")
    if region_group == "europe" and user_row.get("pref_europe", 0) == 1:
        parts.append("matches your preference for Europe")

    # Cultural and language compatibility
    cult_pref = user_row.get("cultural_preference", "")
    if (
        isinstance(cult_pref, str)
        and "arabic" in cult_pref.lower()
        and country_row.get("cultural_compatibility_score", 0) > 0.7
    ):
        parts.append("has strong Arabic and cultural similarity")

    if user_row.get("lang_english", 0) == 1 and country_row.get(
        "cultural_compatibility_score", 0
    ) > 0.3:
        parts.append("supports English or mixed language environments")

    # Budget
    if budget is not None and min_budget is not None:
        try:
            budget_val = float(budget)
            min_budget_val = float(min_budget)
            if budget_val >= min_budget_val:
                parts.append("fits your stated monthly budget")
            else:
                parts.append("may be challenging given your budget")
        except Exception:
            pass

    # Diaspora
    if country_row.get("diaspora_presence_score", 0) >= 0.6:
        parts.append("has a significant Sudanese community")

    # Safety
    if country_row.get("safety_index", 0) >= 0.7:
        parts.append("offers relatively higher safety and stability")

    if not parts:
        return "Recommended based on overall fit with your preferences and constraints."

    return "Recommended because " + ", ".join(parts) + "."


# --------------------------------------------------------------------------
# Main recommendation function
# --------------------------------------------------------------------------


def recommend_destinations(
    user_features: Union[pd.Series, dict],
    country_df: pd.DataFrame,
    user_feature_cols: Sequence[str],
    country_feature_cols: Sequence[str],
    scaler: StandardScaler,
    nn_model: MLPRegressor,
    top_k: int = 5,
    alpha: float = 0.5,
    id_col: str = "country_code",
) -> pd.DataFrame:
    """
    Rank destination countries for a single user.

    Parameters
    ----------
    user_features : Series or dict
        Single user feature row. Should include all columns in user_feature_cols,
        and optionally some raw fields for explanations (budget_estimated_usd, etc).
    country_df : DataFrame
        Destination country features, one row per country.
    user_feature_cols : list[str]
        Columns from user_features to use in the model input.
    country_feature_cols : list[str]
        Columns from country_df to use in the model input.
        id_col can appear in this list but will be excluded from numeric features.
    scaler : StandardScaler
        Fitted scaler from training.
    nn_model : MLPRegressor
        Fitted neural network model.
    top_k : int
        How many destinations to return.
    alpha : float
        Weight between baseline and NN scores:
        final_score = alpha * baseline + (1 - alpha) * nn_score.
    id_col : str
        Column to use as destination identifier (code or name).

    Returns
    -------
    DataFrame
        Top-k recommendations with columns:
        [country_code, country_name, nn_score, baseline_score, final_score, explanation]
    """
    if isinstance(user_features, dict):
        user_row = pd.Series(user_features)
    else:
        user_row = user_features

    # Extract numeric user vector for modeling
    user_num = user_row.reindex(user_feature_cols)
    user_num_df = pd.DataFrame([user_num])

    # Build country numeric feature block
    numeric_country_cols = [c for c in country_feature_cols if c != id_col]
    country_numeric = country_df[numeric_country_cols].copy()

    # Repeat user row for all countries
    n_countries = len(country_numeric)
    user_pairs = pd.concat([user_num_df] * n_countries, ignore_index=True)

    X_pairs = pd.concat(
        [user_pairs, country_numeric.reset_index(drop=True)], axis=1
    )

    # Handle missing values then align columns with scaler
    X_pairs_filled = X_pairs.fillna(X_pairs.median(numeric_only=True))
    X_scaled = prepare_features_for_model(X_pairs_filled, scaler)

    # Neural network predicted scores
    nn_scores = nn_model.predict(X_scaled)

    # Baseline heuristic scores
    baseline_scores = []
    for i in range(n_countries):
        c_row = country_numeric.iloc[i]
        baseline_scores.append(baseline_proxy_score(user_row, c_row))

    baseline_arr = np.array(baseline_scores, dtype=float)

    # Combine scores
    final_scores = alpha * baseline_arr + (1.0 - alpha) * nn_scores

    # Build result DataFrame
    country_id = country_df[id_col] if id_col in country_df.columns else country_df.index
    country_name = (
        country_df["country_name"]
        if "country_name" in country_df.columns
        else country_id
    )

    result = pd.DataFrame(
        {
            "country_code": country_id,
            "country_name": country_name,
            "nn_score": nn_scores,
            "baseline_score": baseline_arr,
            "final_score": final_scores,
        }
    )

    # Generate explanations
    explanations = []
    for i in range(len(result)):
        c_full_row = country_df.iloc[i]
        explanations.append(generate_explanation(user_row, c_full_row))

    result["explanation"] = explanations

    # Sort and keep top-k
    result = result.sort_values("final_score", ascending=False).reset_index(drop=True)
    return result.head(top_k)
