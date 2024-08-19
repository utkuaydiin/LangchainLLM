from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.1)
#messages = [
#    SystemMessage(content="Translate the following from english to Italian"),
#    HumanMessage(content="Hi!"),
#]

system_prompt = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt), ("user", "{text}")
    ]
)
parser = StrOutputParser()

#response = model.invoke(messages)

#prompt_template'ı alıp modele verir modelin çıktısını da parsera verir kullanıcı parser çıktısını görür
chain = prompt_template | model | parser

if __name__ == "__main__":
    print(chain.invoke({"language" : "italian", "text" : "Hello World" }))
