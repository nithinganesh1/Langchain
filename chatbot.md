# Creating a New Chatbot using OpenAI and LangChain

## 1. Prerequisites & Setup
Before building a chatbot, you need to set up your credentials and environment:
- **LangChain Account**: First, create a LangChain account and generate a LangChain API key.
- **LLM API Key**: Obtain an API key for your chosen LLM model (e.g., OpenRouter, OpenAI, Anthropic).
- **Environment Variables**: Create a `.env` file in your project to securely store your credentials:
  ```env
  LANGCHAIN_API_KEY="your_langchain_api_key_here"
  LANGCHAIN_PROJECT="your_project_name"
  OPENAI_API_KEY="your_openai_api_key_here"
  ```

## 2. Calling the API
Calling an LLM API through LangChain is a straightforward task. However, since LangChain contains a vast ecosystem of modules, it is important to know which modules to use for different tasks and what specific dependencies are required for each API call.

## 3. Core LangChain Modules
Here are the essential modules commonly used for building a basic chatbot:

- **`ChatOpenAI`**: Used for connecting to OpenAI's models (or compatible endpoints like OpenRouter).
- **`ChatPromptTemplate`**: Used to structure the initial prompt template, defining the format and context of the input given to the model.
- **`StrOutputParser`**: The default parser that extracts the raw string response from the model's output object. You can also create custom parsers to format the output as JSON or specific data structures.

## 4. Chaining it Together (LCEL)
LangChain provides features that allow you to attach these modules together in the form of **Chains** using LangChain Expression Language (LCEL).

A typical, simple chain flow looks like this:
```text
ChatPromptTemplate ➔ LLM (ChatOpenAI) ➔ OutputParser (StrOutputParser)
```

**Example Syntax:**
```python
chain = prompt | llm | output_parser
response = chain.invoke({"input": "Hello, how are you?"})
```
