from langchain_community.document_loaders import WebBaseLoader

webloader = WebBaseLoader('https://timesofindia.indiatimes.com/')

loaded_web_doc = webloader.load()
print(loaded_web_doc)