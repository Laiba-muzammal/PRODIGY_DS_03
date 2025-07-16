import pandas as pd

def load_and_clean_data(csv_file):
    data = pd.read_csv(csv_file)
    cleaned_data = data.drop_duplicates().dropna().reset_index(drop=True)
    return data, cleaned_data
