from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

question = "Suggest a creative name for an AI study assistant."

model_low = ChatGroq(model="openai/gpt-oss-120b", temperature=0)
model_high = ChatGroq(model="openai/gpt-oss-120b", temperature=1)

result_low = model_low.invoke(question)
result_high = model_high.invoke(question)

print("LOW TEMPERATURE:")
print(result_low.content)

print("HIGH TEMPERATURE:")
print(result_high.content)