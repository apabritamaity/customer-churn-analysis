import pandas as pd
from config import PREPROCESSED_DATA_PATH

def preprocess(data):
    data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
    data.drop_duplicates(inplace=True)

    # Drop missing values
    missing_cols = ['MonthlyCharges', 'TotalCharges', 'Dependents']
    data.dropna(subset=missing_cols, inplace=True)

    # Drop unnecessary columns
    data.drop(columns=['customerID'], inplace=True)

    # Export data
    data.to_csv(PREPROCESSED_DATA_PATH, index=False)

    return data