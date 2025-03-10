# [REQUEST]
#   Create LLM Rag APP asking GitHub repo url?
# [RESPONSE]
#   I'll help you create a LLM RAG (Retrieval Augmented Generation) application
#   that can load and query a GitHub repository. Based on the LangChain documentation,
#   here's a comprehensive example:

# [Install required packages]
# pip install langchain langchain-community langchain-openai chromadb

# Required imports
import os
from langchain_community.document_loaders import GitLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Setup steps
def create_github_rag_app(repo_url, branch="master"):
    # 1. Clone the repository
    repo_path = "./example_data/github_repo/"
    
    # Load repository
    loader = GitLoader(
        clone_url=repo_url,
        repo_path=repo_path,
        branch=branch,
        # Optional: filter only specific file types
        file_filter=lambda file_path: file_path.endswith((".py", ".md", ".txt"))
    )
    
    # 2. Load documents
    documents = loader.load()
    
    # 3. Create embeddings
    embeddings = OpenAIEmbeddings()
    
    # 4. Create vector store
    vectorstore = Chroma.from_documents(
        documents=documents, 
        embedding=embeddings
    )
    
    # 5. Create retriever
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    
    # 6. Create LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    # 7. Create prompt template
    prompt = ChatPromptTemplate.from_template("""
    You are an expert code and documentation assistant. 
    Answer the question based ONLY on the following context:
    
    {context}
    
    Question: {question}
    
    If the information is not in the context, say "I cannot find the answer in the repository."
    """)
    
    # 8. Create RAG chain
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain

# Example usage
def main():
    # Set your OpenAI API key
    os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
    
    # Create RAG app for a specific GitHub repo
    repo_url = "https://github.com/langchain-ai/langchain"
    rag_app = create_github_rag_app(repo_url)
    
    # Ask questions
    questions = [
        "What is LangChain used for?",
        "Explain the main components of LangChain",
        "How do I create a basic RAG application?"
    ]
    
    for question in questions:
        print(f"\nQuestion: {question}")
        answer = rag_app.invoke(question)
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
