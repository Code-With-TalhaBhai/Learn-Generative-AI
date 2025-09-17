from dotenv import load_dotenv
import os
from openai import AsyncOpenAI
from agents import Agent,Runner,OpenAIChatCompletionsModel
from agents.run import RunConfig
import asyncio


load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
print(api_key)

provider = AsyncOpenAI(
    api_key=api_key,
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/'
)


model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=provider
)


config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)


async def main():
    agent = Agent(name="Assistant", instructions="You are helpful assistant", model= 'gemini-2.5-flash')

    # Without Streaming
    # result = await Runner.run(agent, 'Write a haiku about recurrsion', run_config=config)
    # print(result.final_output)

    # With Streaming
    result = Runner.run_streamed(agent, 'Write a haiku about recurrsion', run_config=config)
    print(result)
    print()
    async for e in result.stream_events():
        print(e,"|")






asyncio.run(main())