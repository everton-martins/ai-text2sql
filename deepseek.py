import os # Module to get Environment variable

from openai import OpenAI  # Module of openAI to handle a client with model API

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_KEY"),
    base_url="https://api.deepseek.com"
)

def ai_generate_query(sql_prompt):
    """
    Uses an AI model to generate a SQL query based on a schema and a question.
    Args:
        sql_prompt: prompt to be used
    Returns:
        str: Generated SQL query.
    """

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are an expert in SQL."},
            {"role": "user", "content": sql_prompt}
        ],
        max_tokens=150,
        temperature=0
    )

    r = response.choices[0].message.content.strip()


    # Extract the generated SQL query from the response
    if "```" in r:
        r = r.split("```")[1] 
    if r.startswith("sql"):
        r = r[3:]
    
    return r


def ai_generate_answer(result_prompt):
    """
    Uses an AI model to generate a human-readable response based on the question, query, and result.
    Args:
        result_prompt: prompt to be used
    Returns:
        str: A human-readable response.
    """

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": result_prompt}
        ],
        max_tokens=200,
        temperature=0
    )

    r = response.choices[0].message.content.strip()

    return r