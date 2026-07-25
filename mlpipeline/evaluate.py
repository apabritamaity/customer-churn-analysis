import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import (
    roc_auc_score,
    roc_curve,
    precision_score,
    recall_score,
    accuracy_score
)

from config import X_TEST_DATA_PATH, Y_TEST_DATA_PATH
from exporter import export_metrices

X_test = pd.read_csv(X_TEST_DATA_PATH)
y_test = pd.read_csv(Y_TEST_DATA_PATH)

def evaluate(model):

    y_prob = model.predict_proba(X_test)[:, 1]

    ## ROC AUC
    fpr, tpr, thresholds = roc_curve(
        y_test,
        y_prob
    )


    roc_auc = roc_auc_score(
        y_test,
        y_prob
    )

    # Finding best threshold
    J = tpr - fpr
    ix = np.argmax(J)

    best_threshold = thresholds[ix]

    ## Metrics with best threshold
    y_pred = (y_prob>=best_threshold).astype(int)
    recall = recall_score(y_true=y_test, y_pred=y_pred)
    precision = precision_score(y_true=y_test, y_pred=y_pred)
    accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)

    ## Export model artifacts
    metrices = {
        "recall_score": recall,
        "precision_score" : precision,
        "accuracy_score": accuracy,
        "roc_auc_score": roc_auc,
    }

    roc_curve_data = {
        "fpr": fpr, "tpr": tpr, "thresholds":thresholds
    }

    export_metrices(metrices, roc_curve_data, best_threshold)

    return metrices