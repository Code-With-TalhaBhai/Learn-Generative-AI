import asyncio
from agents import Agent, Runner, WebSearchTool
import os
from dotenv  import load_dotenv

# Ensure your OPENAI_API_KEY is set as an environment variable
# os.environ["OPENAI_API_KEY"] = "your_api_key_here"
load_dotenv()
os.environ.get('OPENAI_API_KEY')


async def main():
    # Define an agent and provide it with the WebSearchTool

    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant that uses web search to answer questions.",
        tools=[WebSearchTool()],
        # Using a model that supports web search is crucial, e.g., gpt-5
        model="gpt-4o-mini", 
    )

    # Run the agent with an input that requires searching the web
    result = await Runner.run(
        agent,
        "What was a positive news story from today?"
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
