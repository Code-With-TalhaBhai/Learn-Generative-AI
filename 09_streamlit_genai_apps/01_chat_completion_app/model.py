from dotenv import load_dotenv,find_dotenv
from openai import OpenAI
from typing import Any
from database import Database 


class MyBotModel:
    def __init__(self,name:str,model:str="gpt-3.5-turbo-1106")->None:
        self.name = name,
        self.model = model,
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

    def get_messages(self):
        return self.messages

    def append_message(self,message):
        self.messages.append(message)

    def send_message(self,message): # Prompt to OpenAI(chat-gpt)
        self.append_message(message)
        # print((self.model)[0])
        # prompt_to_send = {"role":"user","content":"About Agile"}

        stream = self.client.chat.completions.create(
            model=self.model[0],
            messages=[message],
            stream=True
        )
 
        return stream

        
