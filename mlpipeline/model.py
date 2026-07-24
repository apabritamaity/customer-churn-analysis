## Import libraries
import pandas as pd

from sampler import sampling

def model(X_train, y_train):
    y_train = y_train['Churn']
    X_train, y_train = sampling(X_train, y_train)


