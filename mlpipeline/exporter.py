import json
import joblib
import matplotlib.pyplot as plt

from config import (
    MODEL_FILE,
    METADATA_FILE,
    METRICS_DIR
)


def export_model_artifacts(grid_search):

    # Save trained pipeline
    joblib.dump(
        grid_search.best_estimator_,
        MODEL_FILE
    )

    # Save metadata
    metadata = {

        "model_name":
            grid_search.best_estimator_.__class__.__name__,

        "best_params":
            grid_search.best_params_,

        "best_cv_score":
            grid_search.best_score_

    }

    with open(METADATA_FILE, "w") as f:
        json.dump(metadata, f, indent=4)


## Export metrics artifacts
def export_metrices(metrices, roc_curve_data, best_threshold):
    
    with open(METRICS_DIR / "metrices.json", "w") as f:
        json.dump(metrices, f, indent=4)

    with open(METRICS_DIR / "threshold.json", "w") as f:
        json.dump(best_threshold, f)

    # Export ROC curve
    plt.figure(figsize=(8,6))
    plt.plot(
        roc_curve_data["fpr"],
        roc_curve_data["tpr"],
        label=f"AUC = {metrices["roc_auc_score"]:.3f}",
        linewidth=2
    )
    plt.plot(
        [0,1],
        [0,1],
        linestyle="--",
        label="Random Classifier"
    )
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.grid(True)
    plt.savefig(METRICS_DIR / "roc_curve.png", dpi=300, bbox_inches="tight")