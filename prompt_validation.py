from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="Explain {topic} to a {level}",
    input_variables = ["topic", "level"],
    validate_teplate = True
)

provided_variables = {
    "topic" : "Java Inheritance", "level":"Beginner", "name":"Raj"
}
required_vars = set(template.input_variables)
provided_vars = set(provided_variables.keys())

missing = required_vars - provided_vars
extra = provided_vars - required_vars

if missing:
    print(f"Missing variables are, {missing}")
elif extra:
    print(f"Unexpected variables are, {extra}")
else:
    prompt = template.format(**provided_variables)
    print(prompt)


# prompt = template.format(topic="")