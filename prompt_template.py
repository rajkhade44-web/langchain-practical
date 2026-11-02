
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.5,
    max_tokens=150
)

template = PromptTemplate.from_template(
    "Explain {topic} to a {level} using a simple example."
)

prompt = template.format(
    topic="Java inheritance",
    level="beginner"
)

response = model.invoke(prompt)

print(response.content)
