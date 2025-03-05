# AI-Text2SQL

AI-Text2SQL is a project that leverages AI to generate SQL queries from natural language questions and provides human-readable responses based on the query results. 

The goal is to analyze four leading AI models — Google Gemini, OpenAI ChatGPT, DeepSeek, and Alibaba QWEN—focusing on usability, performance, and accuracy.

To test these models, we will develop a simple command-line, allowing non-technical users to interact with a relational database. The dataset used is Netflix show data from [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows).


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [Refs](#Refs)


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/everton-martins/ai-text2sql.git
    cd ai-text2sql
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To use the AI-Text2SQL tool, run the [main.py](http://_vscodecontentref_/0) script with a natural language question as an argument:

```sh
python main.py "What are the top 10 movies on Netflix?"
```

The script will generate an SQL query, execute it on the local SQLite database, and provide a human-readable response based on the query results.

## Configuration

### Import CSV file to SQLite

Before at all, I create a snap code to import CSV to SQLite.

```sh
python importFromCSV.py
```

### Database Schema
The database schema description is stored in the schema_description.txt file. This file needs to accurately describes your SQLite database schema.

### AI Models
The AI ​​models used to generate SQL queries and human-readable responses are imported from four modules. You can switch between AI models by uncommenting the import statement at the top of the main.py file and commenting out the current one.

Each module obtains the model API KEY from an environment variable created by the execution `.env` file.

Don't forget to populate the `.env` file and run it before testing the command line.

[here](#Refs) you will find the procedure to create accounts and keys.

## Examples

### Example 1

Question:

`python3.9 main.py "How many movies was released on 2020?"`

Output:

```
python3.9 main.py "How many movies was released on 2020?"  


 Generated SQL Query: 
SELECT COUNT(*) AS movie_count
FROM titles
WHERE type = 'Movie' AND release_year = 2020;

Response Time: 6.3999 seconds


 Query Result: [(517,)]


 Generated Response: In 2020, a total of 517 movies were released.
Response Time: 1.1784 seconds
Total AI Time: 7.5783 seconds
```

## Code

Key Components in **main.py**

- `get_schema_description()`: Get schema description from file.

- `get_sql_prompt(question)`: Generates the prompt for AI to produce an SQL query.

- `execute_query(query)`: Executes the AI-generated SQL query on SQLite.

- `get_result_prompt(question, query, db_result)`: Constructs a prompt for AI to generate a human-readable response.

In modules named as AI models (example: deepseek.py, gemini.py, chatgpt.py, qwen.py) we implement two simple functions:

 - `ai_generate_query(sql_prompt)`: Uses an AI model to generate a SQL query based on a schema and a question.

 - `ai_generate_answer(result_prompt)`: Uses an AI model to generate a human-readable response based on the question, query, and result.

## Refs

Create API Keys:

- [OpenAI](https://www.youtube.com/watch?v=SzPE_AE0eEo)

- [Google](https://ai.google.dev/gemini-api/docs/api-key)

- [DeepSeek](https://www.youtube.com/watch?v=tRue06PJSRk)

- [Alibaba](https://www.youtube.com/watch?v=QINOR9fATxY)

Datase:

- [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
