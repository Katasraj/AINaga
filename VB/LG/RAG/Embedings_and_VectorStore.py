"""
If you are using the NVIDIA Nemotron model through OpenRouter, then using HuggingFace embeddings is a very good choice.

The important thing to understand is that the LLM and the embedding model do not have to be the same model.

Your architecture can look like this:

PDF/Text
    │
    ▼
Text Splitter
    │
    ▼
Embedding Model (HuggingFace)
    │
    ▼
Chroma Vector Store
    │
    ▼
Retriever
    │
    ▼
NVIDIA Nemotron (OpenRouter)
"""
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from char_text_splitter import text_split

#LLM
llm = ChatOpenAI(
    api_key="api_key",
    base_url="openrouter",
    model="nvidianemotron model"

)

# Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

result1 = text_split()
vector_store = Chroma.from_texts(
    texts=result1,
    embedding=embeddings
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)

# k=3 means the retriever returns the three most relevant chunks.



"""
Why do we need a vector store in RAG?

----Without a vector store----

Question
   ↓
Search all documents
   ↓
Very slow

----With a vector store----

Question
   ↓
Convert to embedding
   ↓
Similarity search
   ↓
Return relevant chunks
   ↓
Send to the LLM
"""


"""
Imagine you have 1,000 pages of a book.

Vector store = a library 🏢
Embeddings = the catalog system 📚
Retriever = the librarian 👨🏻‍🏫
LLM = the teacher 🧠

When you ask a question, the librarian finds the relevant pages, and the teacher answers based on those pages.
"""

