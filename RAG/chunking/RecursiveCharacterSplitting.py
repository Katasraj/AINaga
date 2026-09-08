from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Generative AI is changing the world.
LLMs are becoming powerful.
RAG helps LLMs access private data.
Vector database store embeddings.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(chunk)



