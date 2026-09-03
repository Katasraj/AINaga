from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://docs.langchain.com/oss/python/integrations/document_loaders")

docs = loader.load()


print(docs[0].metadata)
print(100*'*')
print(docs[0].page_content)

