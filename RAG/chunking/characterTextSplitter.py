from langchain_text_splitters import CharacterTextSplitter

text = """
Generative AI is changing the world.
LLMs are becoming powerful.
RAG helps LLMs access private data.
"""

splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=50,
    chunk_overlap=10
)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(chunk)