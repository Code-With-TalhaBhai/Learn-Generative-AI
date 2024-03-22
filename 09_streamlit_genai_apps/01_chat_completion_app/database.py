import shelve

class Database():
    def __init__(self,dbName:str="MY_CHAT_DB")->None:
        self.dbName = dbName

    def load_chat_history(self)->[]:
        with shelve.open(self.dbName) as db:
        # with shelve.open('mydata') as db:
            return db.get('messages',[]) # db.get([key],[value to return if key value is not present])



    def save_chat_history(self,messages:[dict])->None:
        with shelve.open(self.dbName) as db:
            db['messages'] = messages
            db.close()



db = Database()
history = db.load_chat_history()
print(history)