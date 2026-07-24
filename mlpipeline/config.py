from pathlib import Path

# ---------------------------------
# Project Directories
# ---------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent # Create absolute path (root)

DATA_DIR = BASE_DIR / "data"

ARTIFACT_DIR = BASE_DIR / "artifacts"

MODEL_DIR = ARTIFACT_DIR

# ---------------------------------
# Dataset
# ---------------------------------

DATASET_PATH = DATA_DIR / "raw" / "telco_customer_churn.csv"
PREPROCESSED_DATA_DIR =  DATA_DIR / "processed"
PREPROCESSED_DATA_PATH = PREPROCESSED_DATA_DIR / "cleaned_telco_customer_churn.csv"
X_TRAIN_DATA_PATH = PREPROCESSED_DATA_DIR / "X_train.csv"
Y_TRAIN_DATA_PATH = PREPROCESSED_DATA_DIR / "y_train.csv"
X_TEST_DATA_PATH = PREPROCESSED_DATA_DIR / "X_test.csv"
Y_TEST_DATA_PATH = PREPROCESSED_DATA_DIR / "y_test.csv"


TARGET_COLUMN = "Churn"

# ---------------------------------
# Training
# ---------------------------------

TEST_SIZE = 0.20

RANDOM_STATE = 42

# ---------------------------------
# Model
# ---------------------------------

MODEL_NAME = "RandomForest"

THRESHOLD = 0.41

# ---------------------------------
# Artifact Names
# ---------------------------------

PIPELINE_FILE = MODEL_DIR / "pipeline.pkl"

METADATA_FILE = MODEL_DIR / "metadata.json"

FEATURE_FILE = MODEL_DIR / "feature_columns.json"

METRICS_FILE = MODEL_DIR / "metrics.json"