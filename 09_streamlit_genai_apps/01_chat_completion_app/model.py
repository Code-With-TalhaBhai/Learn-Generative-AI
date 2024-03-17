from dotenv import load_dotenv,find_dotenv
from openai import OpenAI
from typing import Any
from database import Database 


class MyBotModel:
    def __init__(self,name:str,model:str="gpt-3.5-turbo-1106")->None:
        self.name:str = name,
        self.model:str = model,
        load_dotenv(find_dotenv())
        self.client:OpenAI = OpenAI()
        self.db = Database()
        self.messages:[dict] = self.load_chat_history()

    def load_chat_history(self)->[dict]:
        return self.db.load_chat_history()

    def save_chat_history(self):
        self.db.save_chat_history(self.messages)
    
    def delete_chat_history(self):
        self.messages = [] # empty the messages
        self.save_chat_history()

    def get_message(self):
        return self.messages

    def append_message(self,message:dict):
        self.messages.append(message)

    def send_message(self,message:dict): # Prompt to OpenAI(chat-gpt)
        self.append_message(message)

        stream = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            stream=True
        )

    # for chunk in stream:
    #     if chunk.choices[0].delta.content is not None:
    #     print(chunk.choices[0].delta.content, end="")

        return stream
        
