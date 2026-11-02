from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b",temperature=0.5, max_tokens=100)

subject = input("Enter your subject:")
level = input("Enter your current level of understanding: ")

question = f"""
    Explain {subject} to a {level}.
    Use simple language and a practical example.
"""

result = model.invoke(question)

print(result.content)

