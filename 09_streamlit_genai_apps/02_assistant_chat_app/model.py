from dotenv import find_dotenv,load_dotenv
from openai import OpenAI
from openai.types.beta.assistant import Assistant
import time


class MessageItem:
    def __init__(self,role,message):
        self.role = role
        self.content = message

class OpenAIBot:
    def __init__(self,name,instructions,model="gpt-3.5-turbo-1106"):
        self.name = name
        self.model = model
        load_dotenv(find_dotenv())
        self.client = OpenAI()
        self.instructions = instructions
        self.assistant = self.client.beta.assistants.create(
            model=self.model,
            instructions=self.instructions,
            name=self.name,
            tools=[{"type":"code_interpreter"}]
        )
        self.messages = []
        self.thread=self.client.beta.threads.create() # Creating thread
        # self.add_message(MessageItem(role='user',message=message))
        # print('total messages are: ',self.messages)


    def get_name(self):
        return self.name
    
    def get_instructions(self):
        return self.instructions
    
    def get_model(self):
        return self.model
    
    def add_message(self,message_item):
        self.messages.append(message_item)

    def get_messages(self):
        return self.messages
    

    def send_message(self,message):
        # Attaching message to thread
        latest_message = self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=message
        )

        run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id,
        )

        self.latest_run = dict(run)
        # print('run is',self.latest_run)
        self.add_message(MessageItem(role='user',message=message))


    def isRunCompleted(self):
        # try:
        while(self.latest_run['status'] != 'completed'):
            time.sleep(1)
            
            run = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread.id,
                run_id=self.latest_run['id']
            )
            self.latest_run = dict(run)
            # print('run is',self.latest_run)

        return True
        # except Exception as e:
            # print('Error in running',e)
            # return False
    
    
    def get_latest_response(self):
        response = self.client.beta.threads.messages.list(
            thread_id=self.thread.id
        )

        
        # return response.data
        msg = MessageItem(role=response.data[0].role,message=response.data[0].content[0].text.value)
        print('msg',msg.content)
        self.add_message(msg)
        print('total msg are',self.messages)
        return msg


