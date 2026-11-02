from langchain_groq import ChatGroq
from dotenv import load_dotenv

# import requests
# import os

# api_key = os.environ.get("GROQ_API_KEY")
# url = "https://api.groq.com/openai/v1/models"

# headers = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }

# response = requests.get(url, headers=headers)

# print(response.json())


load_dotenv()

model = ChatGroq(
    model= "openai/gpt-oss-120b",
    temperature=0
)

result = model.invoke("What is LangChain? Explain in simple language.")
print(result.content)