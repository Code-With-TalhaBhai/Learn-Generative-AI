import chainlit as cl
from agents import Agent, Runner, OpenAIChatCompletionsModel, FunctionTool
from agents.run import RunConfig
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')



check what was my last message