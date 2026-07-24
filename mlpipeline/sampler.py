## Import libraries
import pandas as pd
from imblearn.over_sampling import SMOTE

def sampling(X_train, y_train):
    ## Resample 
    smote = SMOTE(random_state=0)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
    return (X_train_resampled, y_train_resampled)


    
