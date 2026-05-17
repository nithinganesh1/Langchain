from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAPI_KEY")

app = Flask(__name__)

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Question: {question}")
])

# LLM
llm = ChatOpenAI(
    model="deepseek/deepseek-v4-flash",
    base_url="https://openrouter.ai/api/v1",
    temperature=0.7,
    max_tokens=150
)

# Chain
output_parser = StrOutputParser()
chain = prompt | llm | output_parser


@app.route("/", methods=["GET", "POST"])
def index():

    response = ""

    if request.method == "POST":

        user_input = request.form["question"]

        response = chain.invoke({
            "question": user_input
        })

    return render_template("index.html", response=response)


if __name__ == "__main__":
    app.run(debug=True)