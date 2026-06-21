from google import genai


def generate_ai_insight(api_key, prompt):
    """
    Generate AI insight using Gemini API.
    """
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text