import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import (
    create_stuff_documents_chain,
)

from langchain_core.prompts import ChatPromptTemplate

# -----------------------------------------------------
# Load the API key
# -----------------------------------------------------

load_dotenv()

api_key = "api_key"

# -----------------------------------------------------
# Load the PDF
# -----------------------------------------------------

loader = PyPDFLoader("Terms.pdf")
documents = loader.load()

# -----------------------------------------------------
# Split the document into chunks
# -----------------------------------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

# -----------------------------------------------------
# Create embeddings
# -----------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------------------------------
# Create the FAISS vector database
# -----------------------------------------------------

vector_store = FAISS.from_documents(
    chunks,
    embeddings
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)

# -----------------------------------------------------
# Create the LLM
# -----------------------------------------------------

llm = ChatOpenAI(
    api_key="api_key",
    base_url="openrouter",
    model="nvidianemotron model"

)

# -----------------------------------------------------
# Create the prompt
# -----------------------------------------------------

prompt = ChatPromptTemplate.from_template(
    """
Use the following context to answer the question.

Context:
{context}

Question:
{input}
"""
)

# -----------------------------------------------------
# Create the chain
# -----------------------------------------------------

document_chain = create_stuff_documents_chain(
    llm,
    prompt
)

retrieval_chain = create_retrieval_chain(
    retriever,
    document_chain
)

# -----------------------------------------------------
# Ask a question
# -----------------------------------------------------

question = "What is Non-Refundable according to the document"

response = retrieval_chain.invoke(
    {"input": question}
)

print(response["answer"])


"""
Above pipeline is essentially doing this

Terms.pdf
     │
     ▼
Load document
     │
     ▼
Split into chunks
     │
     ▼
Generate embeddings
     │
     ▼
Store vectors in FAISS
     │
     ▼
Retrieve relevant chunks
     │
     ▼
Send the context to Nemotron
     │
     ▼
Generate the answer
"""


"""
    Component	                                Purpose
create_stuff_documents_chain()	        Sends documents to the LLM
create_retrieval_chain()	            Connects the retriever to the LLM
retriever	                            Finds relevant chunks
llm	                                    Generates the answer
prompt	                                Instructs the model
"""