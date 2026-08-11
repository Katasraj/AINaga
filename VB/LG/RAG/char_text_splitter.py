from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(chunk_size=10, chunk_overlap=0, separator=" ")

def text_split():

    text = """
     Prime Minister Narendra Modi on Saturday inaugurated the Alluri Sitarama Raju International Airport at
     Bhogapuram in Andhra Pradesh's Vizianagaram district, a nearly Rs 5,000 crore project that the
     state government says will transform North Andhra into a major economic and industrial hub. Calling the airport a key
     milestone in the state's growth story, the PM said the NDA government was working at "double speed"for the state's development."""

    result1 = splitter.split_text(text)
    return result1
# r = text_split()
# print(r)