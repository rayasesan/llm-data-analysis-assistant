def build_insight_prompt(dataset_context):
    """
    Build prompt for generating automated dataset insights.
    """
    prompt = f"""
You are a professional data analyst.

Analyze the following dataset context and generate clear, practical insights.

Dataset Context:
{dataset_context}

Please provide the analysis in this structure:

1. Dataset Overview
Explain what the dataset appears to contain.

2. Data Quality Observations
Mention missing values, duplicate rows, or potential issues.

3. Key Patterns
Identify important patterns based on the available summary.

4. Business or Analytical Insights
Explain what the data may indicate from a business or analytical perspective.

5. Recommended Next Steps
Suggest further analysis that should be performed.

Rules:
- Do not make unsupported assumptions.
- Base your answer only on the provided dataset context.
- Use clear and professional language.
"""
    return prompt


def build_chat_prompt(dataset_context, user_question):
    """
    Build prompt for answering user questions based on dataset context.
    """
    prompt = f"""
You are a professional data analyst assistant.

Answer the user's question based only on the dataset context provided below.

Dataset Context:
{dataset_context}

User Question:
{user_question}

Rules:
- Do not make unsupported assumptions.
- If the answer cannot be determined from the dataset context, say so clearly.
- Use clear and professional language.
- Provide practical explanation when possible.
"""
    return prompt