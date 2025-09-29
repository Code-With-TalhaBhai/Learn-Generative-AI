import chainlit as cl
from agents import Agent, Runner, OpenAIChatCompletionsModel, FunctionTool
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

agent = Agent(name="chainlit_agent",instructions="You are helpful assistant",model=model)


@cl.on_chat_start
async def chat_start():
    cl.user_session.set('chat_history',[])
    await cl.Message(content='Hi its TalhaGPT, Ask me anything').send()



@cl.on_message
async def on_message(msg:cl.Message):
    history = cl.user_session.get('chat_history')
    history.append({'role':'user','content':msg.content})

    result = await Runner.run(agent,input=history,run_config=config)
    history.append({'role': 'assistant', 'content': result.final_output})
    cl.user_session.set('chat_history',history)
    await cl.Message(content=result.final_output).send()







