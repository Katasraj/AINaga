from langchain_community.document_loaders import PyPDFLoader

def indian_indepenence():

    pdf_loader = PyPDFLoader('Terms.pdf')

    loaded_pdf_doc = pdf_loader.load()
    return loaded_pdf_doc
