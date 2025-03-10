# [REQUEST]
#   Create sample code to query SQLite database by LLM, LangChain and SQLDatabaseChain?
# [RESPONSE]
#   I'll provide a comprehensive example of querying a SQLite database using
#   LangChain's SQLDatabaseChain with step-by-step explanations:

# [Install required packages]
# pip install langchain langchain-community langchain-openai sqlalchemy

# Import required libraries
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain

# 1. Create a connection to the SQLite database
# Replace 'path/to/your/database.db' with the actual path to your SQLite database
db = SQLDatabase.from_uri("sqlite:///path/to/your/database.db")

# 2. Initialize the Language Model
# You can adjust the temperature and model as needed
llm = ChatOpenAI(
    model="gpt-3.5-turbo",  # Choose your preferred OpenAI model
    temperature=0  # Set to 0 for more deterministic responses
)

# 3. Create the SQL Database Chain
db_chain = SQLDatabaseChain.from_llm(
    llm, 
    db, 
    verbose=True  # Enables detailed output of the chain's reasoning
)

# 4. Example queries
def query_database(question):
    """
    Helper function to run queries against the database
    
    Args:
        question (str): Natural language question about the database
    
    Returns:
        The answer to the query
    """
    try:
        result = db_chain.run(question)
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# 5. Example usage
if __name__ == "__main__":
    # Example queries
    queries = [
        "What is the total number of records in the Customers table?",
        "List the top 3 most expensive products",
        "Find the average price of products in each category"
    ]
    
    # Run each query and print results
    for query in queries:
        print(f"\nQuery: {query}")
        result = query_database(query)
        print(f"Result: {result}")

# [Error Handling Example]
# def safe_query_database(question):
#     try:
#         # Add input sanitization if needed
#         if not question or len(question) > 500:
#             raise ValueError("Invalid query length")
        
#         result = db_chain.run(question)
#         return result
#     except Exception as e:
#         print(f"Query failed: {e}")
#         # Log the error or handle it appropriately
#         return None
