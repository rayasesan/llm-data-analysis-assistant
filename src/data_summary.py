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

def get_correlation_summary(df):
    """
    Return top correlations between numeric columns.
    """
    numeric_df = df.select_dtypes(include=["number"])

    if numeric_df.shape[1] < 2:
        return None

    correlation_matrix = numeric_df.corr()

    correlation_pairs = []

    columns = correlation_matrix.columns

    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            correlation_pairs.append({
                "Feature 1": columns[i],
                "Feature 2": columns[j],
                "Correlation": round(correlation_matrix.iloc[i, j], 4),
                "Absolute Correlation": abs(round(correlation_matrix.iloc[i, j], 4))
            })

    correlation_summary = pd.DataFrame(correlation_pairs)

    if correlation_summary.empty:
        return None

    correlation_summary = correlation_summary.sort_values(
        by="Absolute Correlation",
        ascending=False
    ).drop(columns=["Absolute Correlation"])

    return correlation_summary.head(10)