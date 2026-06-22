import pandas as pd


def load_csv(uploaded_file):
    """
    Load uploaded CSV file into a pandas DataFrame.
    Automatically detects common CSV delimiters.
    """
    try:
        df = pd.read_csv(uploaded_file, sep=None, engine="python")
        return df

    except Exception:
        uploaded_file.seek(0)
        df = pd.read_csv(uploaded_file, delimiter=";")
        return df