import os # Module to get Environment variable
import google.generativeai as genai # Module to handle with http model API

# Set up the API key
genai.configure(api_key=os.getenv("GEMINI_KEY"))

# Initialize the model
client = genai.GenerativeModel("gemini-2.0-flash")


def ai_generate_query(sql_prompt):
    """
    Uses an AI model to generate a SQL query based on a schema and a question.
    Args:
        sql_prompt: prompt to be used
    Returns:
        str: Generated SQL query.
    """
    messages = [
        {'role':'model', 'parts': ["You are an expert in SQL."]},
        {'role':'user', 'parts': [sql_prompt]},
    ]

    response = client.generate_content(
        messages,
        generation_config=genai.types.GenerationConfig(
            # Only one candidate for now.
            candidate_count=1,
            max_output_tokens=150,
            temperature=0)
        )

    r = response.text.strip()
    if "```" in r:
        r = r.split("```")[1] 
    if r.startswith("sql"):
        r = r[3:]

    # Extract the generated SQL query from the response
    return r

def ai_generate_answer(result_prompt):
    """
    Uses an AI model to generate a human-readable response based on the question, query, and result.
    Args:
        result_prompt: prompt to be used
    Returns:
        str: A human-readable response.
    """
    messages = [
        {'role':'model', 'parts': ["You are a helpful assistant."]},
        {'role':'user', 'parts': [result_prompt]},
    ]

    response = client.generate_content(
        messages,
        generation_config=genai.types.GenerationConfig(
            # Only one candidate for now.
            candidate_count=1,
            max_output_tokens=200,
            temperature=0)
        )

    return response.text



