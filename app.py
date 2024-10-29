from langchain_ollama import OllamaLLM
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.1")
parser = StrOutputParser()

system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

chain = prompt_template | model | parser

print(chain.invoke({"language": "welsh", "text": "Hi!"}))