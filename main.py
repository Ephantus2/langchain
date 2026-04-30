from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature = 0.7
)

prompt = PromptTemplate.from_template("Explain {topic} simply")

text = prompt.format(topic = "Python loops")

response = llm.invoke(text)

print(response.content)

