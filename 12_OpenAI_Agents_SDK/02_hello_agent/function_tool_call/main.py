import chainlit as cl
from agents import Agent, Runner, OpenAIChatCompletionsModel, function_tool
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



@function_tool
def weather_tool(city:str):
    return f'The weather in {city} is 22 degree celsius'


@function_tool
def student_finder(roll_no):
    data = {
        1: 'Talha',
        2: 'Fazal',
        3: 'Qasim'
    }

    return data[roll_no]

agent = Agent(name="chainlit_agent",instructions="You are helpful assistant",tools=[weather_tool,student_finder])


@cl.on_chat_start
async def chat_start():
    await cl.Message(content='Hello, This is TalhaGPT. Ask me anything').send()



@cl.on_message
async def on_message(msg:cl.Message):
    result = await Runner.run(agent,input=msg.content,run_config=config)
    await cl.Message(content=result.final_output).send()







