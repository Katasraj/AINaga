from dotenv import load_dotenv
import os

load_dotenv()

print("API key exists:", bool(os.getenv("GROQ_API_KEY")))
print("API key starts with:", os.getenv("GROQ_API_KEY", "")[:8])



# from dotenv import load_dotenv
# from groq import Groq
# import os
#
# load_dotenv()
#
# api_key = os.getenv("GROQ_API_KEY")
#
# print("API key exists:", bool(api_key))
# print("API key prefix:", api_key[:10] if api_key else None)
#
# client = Groq(api_key=api_key)
#
# models = client.models.list()
#
# for model in models.data:
#     print(model.id)