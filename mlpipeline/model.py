## Import libraries
import pandas as pd

from sampler import sampling
from tuner import hypertuning

def train(X_train, y_train):
    # y_train = y_train['Churn'] # converting dataframe to series
    X_train, y_train = sampling(X_train, y_train) # applying SMOTE
    best_model = hypertuning(X_train=X_train, y_train=y_train) # performing hyperparameter tuning

    return best_model


