import pandas as pd


def get_dataset_overview(df):
    """
    Return basic dataset overview.
    """
    return {
        "total_rows": df.shape[0],
        "total_columns": df.shape[1],
        "duplicate_rows": df.duplicated().sum()
    }


def get_column_data_types(df):
    """
    Return column names and their data types.
    """
    return pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str).values
    })


def get_descriptive_statistics(df):
    """
    Return descriptive statistics for numeric columns.
    """
    numeric_columns = df.select_dtypes(include=["number"])

    if numeric_columns.empty:
        return None

    return numeric_columns.describe()