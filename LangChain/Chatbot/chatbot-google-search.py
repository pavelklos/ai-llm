# [REQUEST]
#   Create AI LLM Agent App. It search by OpenAI LLM
#   or by Serper API Agent (Google Search API)for user question?
# [RESPONSE]
#   I'll help you create an AI LLM Agent App that can search using either OpenAI's LLM
#   or the Serper Google Search API. Here's a comprehensive example:

# [Install required packages]
# pip install langchain langchain-openai langchain-community serpapi

import os
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SerperAPIWrapper
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.tools import DuckDuckGoSearchTool

# Set up API keys
def set_api_keys():
    # OpenAI API Key
    if "OPENAI_API_KEY" not in os.environ:
        os.environ["OPENAI_API_KEY"] = input("Enter your OpenAI API Key: ")
    
    # Serper API Key (optional)
    if "SERPAPI_API_KEY" not in os.environ:
        os.environ["SERPAPI_API_KEY"] = input("Enter your Serper API Key (optional): ")

# Create search tools
def create_search_tools():
    tools = []
    
    # OpenAI Search (via DuckDuckGo)
    ddg_search = DuckDuckGoSearchTool()
    tools.append(
        Tool(
            name="OpenAI Search",
            func=ddg_search.run,
            description="Useful for searching the web using DuckDuckGo"
        )
    )
    
    # Serper Google Search (if API key is available)
    try:
        serper_search = SerperAPIWrapper()
        tools.append(
            Tool(
                name="Serper Google Search",
                func=serper_search.run,
                description="Useful for searching the web using Google via Serper API"
            )
        )
    except Exception as e:
        print(f"Serper API not configured: {e}")
    
    return tools

# Create the agent
def create_search_agent(search_type='openai'):
    # Initialize the language model
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    
    # Get search tools
    tools = create_search_tools()
    
    # Initialize the agent
    agent = initialize_agent(
        tools, 
        llm, 
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        verbose=True
    )
    
    return agent

# Main interaction function
def main():
    # Set up API keys
    set_api_keys()
    
    # Create the agent
    agent = create_search_agent()
    
    # Interactive loop
    while True:
        try:
            # Get user input
            user_query = input("\nEnter your question (or 'quit' to exit): ")
            
            # Check for exit
            if user_query.lower() == 'quit':
                break
            
            # Run the agent
            response = agent.run(user_query)
            
            # Print the response
            print("\nAgent Response:")
            print(response)
        
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the application
if __name__ == "__main__":
    main()

# [REQUEST]
#   I want to use SERPER API (serper.dev), NOT use SerpApi (serpapi.com),
#   do refactoring please?
# [RESPONSE]
#   You're right. Here's a refactored version specifically using
#   the Serper Google Search API from serper.dev:

import os
from langchain_openai import ChatOpenAI
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import initialize_agent, Tool, AgentType

class SearchAgent:
    def __init__(self):
        # Validate and set API keys
        self.validate_api_keys()
        
        # Initialize language model
        self.llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
        
        # Create search tool
        self.search_tool = self.create_serper_search_tool()
        
        # Initialize agent
        self.agent = self.create_search_agent()

    def validate_api_keys(self):
        """Validate and set required API keys"""
        # Check OpenAI API Key
        if "OPENAI_API_KEY" not in os.environ:
            os.environ["OPENAI_API_KEY"] = input("Enter your OpenAI API Key: ")
        
        # Check Serper API Key
        if "SERPER_API_KEY" not in os.environ:
            os.environ["SERPER_API_KEY"] = input("Enter your Serper API Key: ")

    def create_serper_search_tool(self):
        """Create Serper Google Search tool"""
        try:
            serper_search = GoogleSerperAPIWrapper()
            return Tool(
                name="Google Search",
                func=serper_search.run,
                description="Useful for searching the web using Google via Serper API. Input should be a search query."
            )
        except Exception as e:
            print(f"Error creating Serper search tool: {e}")
            return None

    def create_search_agent(self):
        """Create an agent with Serper search tool"""
        # Prepare tools
        tools = [self.search_tool] if self.search_tool else []
        
        # Initialize agent
        return initialize_agent(
            tools, 
            self.llm, 
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
            verbose=True
        )

    def run_query(self, query):
        """Run a search query"""
        try:
            return self.agent.run(query)
        except Exception as e:
            return f"An error occurred: {e}"

def main():
    # Create search agent
    search_agent = SearchAgent()
    
    # Interactive loop
    while True:
        # Get user input
        user_query = input("\nEnter your question (or 'quit' to exit): ").strip()
        
        # Check for exit
        if user_query.lower() in ['quit', 'exit', 'q']:
            break
        
        # Run query and print response
        response = search_agent.run_query(user_query)
        print("\nAgent Response:")
        print(response)

if __name__ == "__main__":
    main()
