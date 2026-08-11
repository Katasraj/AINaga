from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import (
    create_stuff_documents_chain,
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)

from langchain_community.vectorstores import FAISS

print("Everything is working.")