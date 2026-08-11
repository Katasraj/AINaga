from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key="api_key",
    base_url="openrouter",
    model="nvidianemotron model"

)


response = llm.invoke("What is Tavily?")

print(response.content)

'''
Can I replace Gemini with the NVIDIA model?

Yes, for tasks such as:

✅ Chatbots
✅ Question answering
✅ Tavily agents
✅ RAG (Retrieval-Augmented Generation)
✅ Document summarization
✅ Code generation
✅ Python coding assistance
✅ SQL generation
✅ Email writing
✅ OCR text analysis (after OCR is done)
✅ Image understanding (if the model supports vision; the specific NVIDIA model you're using is text-only)
'''

# Build model-independent Tavily framework