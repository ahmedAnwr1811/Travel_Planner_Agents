import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool

# Load environment variables
load_dotenv()

# Retrieve API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# Validate API keys
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not set in .env file")
if not SERPER_API_KEY:
    raise ValueError("SERPER_API_KEY not set in .env file")

# Initialize LLM
llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model_name="gpt-4o-mini",
    temperature=0.7,
    max_tokens=4096
)

# Initialize search tool
search_tool = SerperDevTool(api_key=SERPER_API_KEY)