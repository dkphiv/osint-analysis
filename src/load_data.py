import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df = df[['body', 'created_utc']]
    df.dropna(inplace=True)
    return df