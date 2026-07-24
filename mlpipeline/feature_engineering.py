import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder
from sklearn.preprocessing import StandardScaler

from config import X_TRAIN_DATA_PATH, X_TEST_DATA_PATH, Y_TRAIN_DATA_PATH, Y_TEST_DATA_PATH

def engineer_features(data):
    # Split features and target
    X, y = data.iloc[:, :-1], data.iloc[:,-1]

    # Split the dataset into training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Categorical Featues
    cat_features = X_train.select_dtypes(include=['object']).columns

    # Numerical features
    num_features = X_train.select_dtypes(exclude='object').columns


    ## Encode binary features
    binary_feat = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaperlessBilling']

    # Encode binary cat cols manually except 'gender'
    X_train[binary_feat[1:]]= X_train[binary_feat[1:]].map(lambda x: 1 if x=='Yes' else 0)
    X_test[binary_feat[1:]]= X_test[binary_feat[1:]].map(lambda x: 1 if x=='Yes' else 0)

    # Encode 'gender' with OneHotEncoder
    ohe = OneHotEncoder(sparse_output=False, drop='first')
    X_train['gender']=ohe.fit_transform(X_train[['gender']])
    X_test['gender']=ohe.transform(X_test[['gender']])


    ## Encode multiple categorical features
    non_binary_cats = ['InternetService', 'Contract', 'PaymentMethod']

    # OneHotEncoding
    ohe = OneHotEncoder(sparse_output=False, drop='first').set_output(transform="pandas")

    # Encode
    ohe_encoded_X_train = ohe.fit_transform(X_train[non_binary_cats])
    ohe_encoded_X_test = ohe.transform(X_test[non_binary_cats])


    ## Added to the original dataframe
    X_train = X_train.drop(columns=non_binary_cats).join(ohe_encoded_X_train)
    X_test = X_test.drop(columns=non_binary_cats).join(ohe_encoded_X_test)


    ## Encode the target col
    le = LabelEncoder()
    y_train = le.fit_transform(y_train)
    y_test = le.transform(y_test)


    ## Scaling except target
    scaler = StandardScaler()
    for col in num_features[1:]:
        X_train[col] = scaler.fit_transform(X_train[[col]])
        X_test[col] = scaler.transform(X_test[[col]])


    ## Convert y_train and y_test data from numpy array to pandas series format
    y_train_series = pd.Series(y_train, name='Churn')
    y_test_series = pd.Series(y_test, name='Churn')


    ## Export feature engineered files
    X_train.to_csv(X_TRAIN_DATA_PATH, index=False)
    X_test.to_csv(X_TEST_DATA_PATH, index=False)
    y_train_series.to_csv(Y_TRAIN_DATA_PATH, index=False)
    y_test_series.to_csv(Y_TEST_DATA_PATH, index=False)

    return (X_train, y_train)

   