"""Module to handle with local database sqlite"""
import sqlite3
import sys
from timeit import default_timer as timer

#from chatgpt import ai_generate_answer, ai_generate_query
#from gemini import ai_generate_answer, ai_generate_query
#from deepseek import ai_generate_answer, ai_generate_query
from qwen import ai_generate_answer, ai_generate_query


def get_schema_description():
    """
    Load table description from file
    Returns:
        str: Schema description.
    """
    schema_description_file = "schema_description.txt"
    with open(schema_description_file, "r", encoding="utf-8") as file:
        return file.read()


def get_sql_prompt(question):
    """
    Load AI prompt to generate SQL query
    Args:
        question: users question
    Returns:
        str: AI prompt to generate SQL.
    """
    sql_prompt = "You are an expert in SQL. Given the following database schema in SQLite:\n\n"
    sql_prompt += get_schema_description()
    sql_prompt += "\nWrite an SQL query that answers the following question:\n\n"
    sql_prompt += question
    sql_prompt += "\n\nSQL Query:"
    return sql_prompt


def get_result_prompt(question, query, db_result):
    """
    Load AI prompt to answare question based on SQL result
    Args:
        question: users question
        query: SQL query executed
        db_result: SQL result
    Returns:
        str: AI prompt to generate asware.
    """
    result_prompt = "You are an assistant who explains database query results in English.\n\n"
    result_prompt += f"\n\nThe user asked: '{question}'\n\n"
    result_prompt += f"The SQL query executed was:\n{query}\n\n"
    result_prompt += "The result of the query was:\n"
    result_prompt += f"{db_result}"
    result_prompt += "\n\nBased on this information, provide a clear and concise response to the user."
    return result_prompt


def execute_query(query):
    """
    Execute SQL query on SQLite
    Args:
        query: SQL query 
    Returns:
        set: Result
    """
    conn = sqlite3.connect("netflix_titles.db")
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    conn.close()
    return result


def main():
    """
    Main function
    """
    question = sys.argv[1]

    start_time = timer()
    # Generate SQL query using AI
    query = ai_generate_query(get_sql_prompt(question))
    end_time = timer()
    generate_query_rt = end_time - start_time
    print("\n\n Generated SQL Query:", query)
    print(f"Response Time: {generate_query_rt:.4f} seconds")


    # Execute query and fetch results
    db_result = execute_query(query)
    # Display results
    print("\n\n Query Result:", db_result)

    start_time = timer()
    # Generate human-readable response using AI
    response = ai_generate_answer(
        get_result_prompt(question, query, db_result))
    end_time = timer()
    generate_answer_rt = end_time - start_time
    print("\n\n Generated Response:", response)
    print(f"Response Time: {generate_answer_rt:.4f} seconds")

    print(f"Total AI Time: {generate_query_rt+generate_answer_rt:.4f} seconds")

if __name__ == "__main__":
    main()
