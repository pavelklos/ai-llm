# [REQUEST]
#   Create basic RAG App with PDF locally and FAISS vector store, save and load vector store?
# [RESPONSE]
#   I'll provide a comprehensive example of creating a RAG application with a PDF,
#   using FAISS as the vector store, and demonstrating how to save and load the vector store.
#   Here's a step-by-step implementation:

# [Install required packages]
# pip install langchain-community langchain-openai faiss-cpu pypdf langchain-text-splitters

import os
import getpass
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Set up OpenAI API Key
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter OpenAI API Key: ")

# 1. Load the PDF
def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    return pages

# 2. Split the documents
def split_documents(pages):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200
    )
    splits = text_splitter.split_documents(pages)
    return splits

# 3. Create Vector Store
def create_vector_store(splits, embeddings):
    vector_store = FAISS.from_documents(splits, embeddings)
    return vector_store

# 4. Save Vector Store
def save_vector_store(vector_store, path):
    vector_store.save_local(path)
    print(f"Vector store saved to {path}")

# 5. Load Vector Store
def load_vector_store(path, embeddings):
    loaded_store = FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)
    return loaded_store

# 6. Create RAG Chain
def create_rag_chain(vector_store):
    # Retriever
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    
    # Prompt Template
    template = """Answer the question based only on the following context:
    {context}
    
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    
    # LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    
    # RAG Chain
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain

# Main Execution
def main():
    # Path to your PDF
    pdf_path = "path/to/your/document.pdf"
    
    # Embeddings
    embeddings = OpenAIEmbeddings()
    
    # Load and split PDF
    pages = load_pdf(pdf_path)
    splits = split_documents(pages)
    
    # Create Vector Store
    vector_store = create_vector_store(splits, embeddings)
    
    # Save Vector Store
    save_vector_store(vector_store, "faiss_index")
    
    # Load Vector Store (simulating a new session)
    loaded_vector_store = load_vector_store("faiss_index", embeddings)
    
    # Create RAG Chain
    rag_chain = create_rag_chain(loaded_vector_store)
    
    # Example Query
    query = "What is the main topic of this document?"
    response = rag_chain.invoke(query)
    print("\nQuery:", query)
    print("\nResponse:", response)

# Run the main function
if __name__ == "__main__":
    main()
