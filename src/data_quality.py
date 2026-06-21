import pandas as pd


def get_missing_values(df):
    """
    Return missing value count and percentage for each column.
    """
    missing_values = df.isnull().sum().reset_index()
    missing_values.columns = ["Column", "Missing Values"]

    missing_values["Missing Percentage"] = (
        missing_values["Missing Values"] / len(df) * 100
    ).round(2)

    return missing_values


def get_duplicate_count(df):
    """
    Return number of duplicate rows.
    """
    return df.duplicated().sum()