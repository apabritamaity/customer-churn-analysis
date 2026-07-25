## Import libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import joblib
from exporter import export_model_artifacts

def hypertuning(X_train, y_train):
    param_grid = {
        'n_estimators': [200,300,400],
        'max_depth': [8, 10,15],
        'min_samples_leaf': [15,18],
        'max_features': ['log2']
    }

    clf_grid = GridSearchCV(
        estimator = RandomForestClassifier(random_state=42),
        param_grid = param_grid,
        cv=5,
        scoring='recall',
        n_jobs=-1
    )

    ## Fit
    clf_grid.fit(X_train, y_train)

    # Export the model artifacts
    export_model_artifacts(grid_search=clf_grid)

    best_clf = clf_grid.best_estimator_
    return best_clf




  



