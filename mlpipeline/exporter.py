import json
import joblib
import config

from ml_pipeline.config import (
    PIPELINE_FILE,
    METADATA_FILE
)


def export_artifacts(grid_search):

    # Save trained pipeline
    joblib.dump(
        grid_search.best_estimator_,
        PIPELINE_FILE
    )

    # Save metadata
    metadata = {

        "model_name":
            type(grid_search.best_estimator_.named_steps["classifier"]).__name__,

        "best_params":
            grid_search.best_params_,

        "best_cv_score":
            grid_search.best_score_

    }

    with open(METADATA_FILE, "w") as f:
        json.dump(metadata, f, indent=4)