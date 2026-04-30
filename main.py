from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature = 0.7
)

prompt = PromptTemplate.from_template("Explain {topic} simply")

chain = prompt | llm | StrOutputParser()



response = chain.invoke({"topic": "Linked Lists"})

print(response)

