import pandas as pd


def load_csv(uploaded_file):
    """
    Load uploaded CSV file into a pandas DataFrame.
    """
    return pd.read_csv(uploaded_file)