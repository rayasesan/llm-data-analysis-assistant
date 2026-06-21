import streamlit as st

from src.data_loader import load_csv
from src.data_summary import (
    get_dataset_overview,
    get_column_data_types,
    get_descriptive_statistics
)
from src.data_quality import get_missing_values
from src.visualization import (
    get_numeric_columns,
    get_categorical_columns,
    create_histogram,
    create_bar_chart,
    create_scatter_plot
)
from src.prompt_template import build_insight_prompt, build_chat_prompt
from src.llm_service import generate_ai_insight


st.set_page_config(
    page_title="LLM Data Analysis Assistant",
    layout="wide"
)


st.title("LLM-Powered Data Analysis Assistant")
st.write(
    "Upload a CSV file to generate a data preview, summary statistics, "
    "data quality checks, interactive visualizations, AI-generated insights, "
    "and dataset question answering."
)


uploaded_file = st.file_uploader(
    label="Upload CSV File",
    type=["csv"]
)


if uploaded_file is not None:
    try:
        df = load_csv(uploaded_file)

        st.success("File uploaded successfully.")

        # Dataset preview
        st.subheader("Dataset Preview")
        st.dataframe(df.head(10), use_container_width=True)

        # Dataset overview
        st.subheader("Dataset Overview")

        overview = get_dataset_overview(df)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Rows", overview["total_rows"])

        with col2:
            st.metric("Total Columns", overview["total_columns"])

        with col3:
            st.metric("Duplicate Rows", overview["duplicate_rows"])

        # Column data types
        st.subheader("Column Data Types")
        column_data_types = get_column_data_types(df)

        st.dataframe(
            column_data_types,
            use_container_width=True
        )

        # Missing value summary
        st.subheader("Missing Value Summary")
        missing_value_summary = get_missing_values(df)

        st.dataframe(
            missing_value_summary,
            use_container_width=True
        )

        # Descriptive statistics
        st.subheader("Descriptive Statistics")

        descriptive_statistics = get_descriptive_statistics(df)

        if descriptive_statistics is not None:
            st.dataframe(
                descriptive_statistics,
                use_container_width=True
            )
        else:
            st.info("No numeric columns available for descriptive statistics.")

        # Data visualization
        st.subheader("Data Visualization")

        numeric_columns = get_numeric_columns(df)
        categorical_columns = get_categorical_columns(df)

        chart_type = st.selectbox(
            "Select Chart Type",
            [
                "Numeric Distribution",
                "Categorical Count",
                "Scatter Plot"
            ]
        )

        if chart_type == "Numeric Distribution":
            if numeric_columns:
                selected_numeric_column = st.selectbox(
                    "Select Numeric Column",
                    numeric_columns
                )

                fig = create_histogram(df, selected_numeric_column)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No numeric columns available for visualization.")

        elif chart_type == "Categorical Count":
            if categorical_columns:
                selected_categorical_column = st.selectbox(
                    "Select Categorical Column",
                    categorical_columns
                )

                fig = create_bar_chart(df, selected_categorical_column)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No categorical columns available for visualization.")

        elif chart_type == "Scatter Plot":
            if len(numeric_columns) >= 2:
                x_column = st.selectbox(
                    "Select X-axis Column",
                    numeric_columns
                )

                y_column = st.selectbox(
                    "Select Y-axis Column",
                    numeric_columns,
                    index=1
                )

                fig = create_scatter_plot(df, x_column, y_column)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("At least two numeric columns are required for a scatter plot.")

        # Dataset context for LLM
        dataset_context = {
            "total_rows": overview["total_rows"],
            "total_columns": overview["total_columns"],
            "duplicate_rows": overview["duplicate_rows"],
            "columns": df.columns.tolist(),
            "data_types": column_data_types.to_dict(orient="records"),
            "missing_values": missing_value_summary.to_dict(orient="records"),
            "descriptive_statistics": (
                descriptive_statistics.to_dict()
                if descriptive_statistics is not None
                else "No numeric columns available"
            )
        }

        # AI insight generator
        st.subheader("AI Insight Generator")

        if st.button("Generate AI Insight"):
            try:
                api_key = st.secrets["GEMINI_API_KEY"]
                prompt = build_insight_prompt(dataset_context)

                with st.spinner("Generating AI insight..."):
                    ai_insight = generate_ai_insight(api_key, prompt)

                st.markdown(ai_insight)

            except KeyError:
                st.error(
                    "Gemini API key is missing. Add GEMINI_API_KEY "
                    "to .streamlit/secrets.toml."
                )

            except Exception as error:
                st.error(f"An error occurred while generating AI insight: {error}")

        # Chat with dataset
        st.subheader("Chat with Dataset")

        user_question = st.text_input(
            "Ask a question about the uploaded dataset"
        )

        if st.button("Submit Question"):
            if user_question.strip():
                try:
                    api_key = st.secrets["GEMINI_API_KEY"]
                    chat_prompt = build_chat_prompt(dataset_context, user_question)

                    with st.spinner("Generating answer..."):
                        ai_answer = generate_ai_insight(api_key, chat_prompt)

                    st.markdown(ai_answer)

                except KeyError:
                    st.error(
                        "Gemini API key is missing. Add GEMINI_API_KEY "
                        "to .streamlit/secrets.toml."
                    )

                except Exception as error:
                    st.error(f"An error occurred while generating the answer: {error}")

            else:
                st.warning("Please enter a question before submitting.")

    except Exception as error:
        st.error(f"An error occurred while processing the file: {error}")

else:
    st.info("Please upload a CSV file to start the analysis.")