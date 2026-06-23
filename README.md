# LLM-Powered Data Analysis Assistant

## Project Overview

LLM-Powered Data Analysis Assistant is an AI-powered data analysis application that allows users to upload CSV files, generate automated exploratory data analysis summaries, detect data quality issues, create interactive visualizations, and ask natural language questions about the dataset using a Large Language Model.

This project is designed to help users understand datasets faster without manually writing extensive analysis code. It combines data analysis workflow, interactive visualization, and LLM-based insight generation in one Streamlit application.

## Objectives  

The objectives of this project are:

* Build an interactive application for CSV-based data analysis.
* Automate basic exploratory data analysis tasks.
* Detect missing values, duplicate records, and data type information.
* Provide descriptive statistics for numeric features.
* Generate interactive visualizations for numeric and categorical variables.
* Use an LLM to generate dataset insights and answer user questions.

## Features

### 1. CSV Upload

Users can upload a CSV file directly through the web application.

### 2. Dataset Preview

The application displays the first rows of the uploaded dataset to help users quickly inspect the data structure.

### 3. Dataset Overview

The application provides basic dataset information, including:

* Total rows
* Total columns
* Duplicate rows

### 4. Column Data Types

The application shows each column name and its corresponding data type.

### 5. Missing Value Summary

The application detects missing values for each column and calculates the missing value percentage.

### 6. Descriptive Statistics

The application generates descriptive statistics for numeric columns, including count, mean, standard deviation, minimum, quartiles, and maximum values.

### 7. Interactive Data Visualization

The application supports several visualization types:

* Numeric distribution
* Categorical count
* Scatter plot

### 8. AI Insight Generator

The application uses a Large Language Model to generate structured insights based on the uploaded dataset summary.

The generated analysis includes:

* Dataset overview
* Data quality observations
* Key patterns
* Business or analytical insights
* Recommended next steps

### 9. Chat with Dataset

Users can ask natural language questions about the uploaded dataset. The assistant answers based on the available dataset context.

Example questions:

* Which columns have missing values?
* Is this dataset ready for machine learning?
* What should I analyze next?
* What are the main data quality issues in this dataset?

### CSV Delimiter Detection

The application supports CSV files with different delimiters, including comma-separated and semicolon-separated datasets.

## Tech Stack

* Python
* Streamlit
* Pandas
* NumPy
* Plotly
* Google Gemini API
* Git and GitHub

## Project Structure

```text
llm-data-analysis-assistant/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── data_loader.py
│   ├── data_summary.py
│   ├── data_quality.py
│   ├── visualization.py
│   ├── llm_service.py
│   └── prompt_template.py
│
├── data/
├── assets/
├── reports/
└── .streamlit/
    └── secrets.toml
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/llm-data-analysis-assistant.git
cd llm-data-analysis-assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

For Git Bash on Windows:

```bash
source venv/Scripts/activate
```

For Command Prompt on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## API Key Setup

This project uses the Gemini API for LLM-based insight generation.

Create a `.streamlit/secrets.toml` file and add your API key:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

Important: Do not upload your API key to GitHub. Make sure `.streamlit/secrets.toml` is listed in `.gitignore`.

## Run the Application

Run the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

## Example Use Case

A user uploads a customer churn dataset. The application will automatically:

1. Preview the dataset.
2. Display dataset size and duplicate rows.
3. Show column data types.
4. Detect missing values.
5. Generate descriptive statistics.
6. Create interactive visualizations.
7. Generate AI-powered insights.
8. Answer questions about the dataset.

## Skills Demonstrated

This project demonstrates skills in:

* Data analysis
* Exploratory data analysis
* Data quality checking
* Data visualization
* LLM integration
* Prompt engineering
* Streamlit application development
* Modular Python project structure
* API key management
* Git and GitHub workflow

## Future Improvements

Potential future improvements include:

* Export analysis report to PDF or HTML.
* Add automated chart recommendation.
* Add correlation analysis.
* Add machine learning readiness checker.
* Add data cleaning recommendations.
* Add session history.
* Support Excel files.
* Support multiple uploaded datasets.

## Project Status

Current status: Minimum viable product completed.

Implemented features:

* CSV upload
* Dataset preview
* Dataset overview
* Column data types
* Missing value summary
* Descriptive statistics
* Interactive visualizations
* AI insight generator
* Chat with dataset

## Author

Raya Sesan Firdaus

Informatics Engineering Student
Data Analyst and Machine Learning Enthusiast
