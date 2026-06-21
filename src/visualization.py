import pandas as pd
import plotly.express as px


def get_numeric_columns(df):
    """
    Return a list of numeric columns.
    """
    return df.select_dtypes(include=["number"]).columns.tolist()


def get_categorical_columns(df):
    """
    Return a list of categorical columns.
    """
    return df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()


def create_histogram(df, column):
    """
    Create a histogram for a numeric column.
    """
    fig = px.histogram(
        df,
        x=column,
        title=f"Distribution of {column}",
        marginal="box"
    )

    return fig


def create_bar_chart(df, column):
    """
    Create a bar chart for a categorical column.
    """
    value_counts = df[column].value_counts().reset_index()
    value_counts.columns = [column, "Count"]

    fig = px.bar(
        value_counts,
        x=column,
        y="Count",
        title=f"Count by {column}"
    )

    return fig


def create_scatter_plot(df, x_column, y_column):
    """
    Create a scatter plot using two numeric columns.
    """
    fig = px.scatter(
        df,
        x=x_column,
        y=y_column,
        title=f"{x_column} vs {y_column}"
    )

    return fig