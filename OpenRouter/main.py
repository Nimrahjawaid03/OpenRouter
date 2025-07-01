from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# Load .env file and get API key
load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# Check if the API key is present; if not, raise an error
if not openrouter_api_key:
    raise ValueError("OPENROUTER_API_KEY is not set. Please ensure it is defined in your .env file.")

#setup Openrouter client (like OpenAI, but via OpenRouter)
external_client = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1",
)

# Choose any openrouter-supported model
model = OpenAIChatCompletionsModel(
    model="google/gemini-2.0-flash-exp:free", # Example model, replace if needed
    openai_client=external_client
)

# Setup config
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Define Agent
agent = Agent(
    name = "Writer Agent",
    instructions = "You are a writer agent. Generate stories,poems, essay etc."
)

# Input and run agent
response = Runner.run_sync(
    agent,
    input="Write a short essay on Quaid-e-Azam in simple English.",
    run_config= config
)

# Output
print(response)