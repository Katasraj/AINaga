from langchain_community.document_loaders import TextLoader


loader = TextLoader('today_news.txt',encoding='utf-8')
docs = loader.load()

print(docs)
print(100*'*')
print(docs[0].metadata)
print(100*'*')
print(docs[0].page_content)

