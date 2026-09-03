from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('machine_learning_short_notes.pdf')
docs = loader.load()


print(docs[0].metadata)
print(100*'*')
print(docs[0].page_content)