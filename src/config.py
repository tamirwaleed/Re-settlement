from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Data paths
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA = DATA_DIR / "raw" / "survey_responses_original.csv"
CLEAN_DATA = DATA_DIR / "intermediate" / "cleaned_responses.csv"
PROCESSED_DATA = DATA_DIR / "processed" / "final_model_dataset.csv"

COUNTRY_FEATURES_CSV = DATA_DIR / "external" / "country_features.csv"

# Models path
MODELS_DIR = PROJECT_ROOT / "models"

RANDOM_SEED = 42