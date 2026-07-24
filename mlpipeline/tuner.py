## Import libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import joblib

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
        n_jobs=-1
    )

    ## Fit
    clf_grid.fit(X_train, y_train)

    ## Get the best model
    best_clf = clf_grid.best_estimator_
    best_params = clf_grid.best_params_

    # Export the model to a file
    joblib.dump(best_clf, '../Artifacts/Model/telco_churn_final_model.pkl')

    return best_clf




  



