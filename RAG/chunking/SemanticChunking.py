from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader

loader = TextLoader(r"C:\Users\Hp\PycharmProjects\Next\RAG\loaders\today_news.txt", encoding='utf-8')
docs = loader.load()

embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

splitter = SemanticChunker(embeddings)

chunks = splitter.split_documents(docs)
print(chunks)