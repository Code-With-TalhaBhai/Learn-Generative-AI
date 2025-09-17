import chainlit as cl
from agents import Agent, Runner, OpenAIChatCompletionsModel
from agents.run import RunConfig
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')



provider = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(model='gemini-2.5-flash',openai_client=provider)

config = RunConfig(model=model,model_provider=provider,tracing_disabled=True)

# agent = Agent(name="chainlit_agent",instructions="You are helpful assistant",model='gemini-2.5-flash')
agent = Agent(name="chainlit_agent",instructions="You are helpful assistant",model=model)


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="New chat has started").send()


@cl.on_message
async def on_message(msg: cl.Message):
    # result = Runner.run_sync(agent,msg.content,run_config=config)
    result = Runner.run_sync(agent,msg.content).final_output
    await cl.Message(content=result).send()



