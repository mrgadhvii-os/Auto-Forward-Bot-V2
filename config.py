from os import environ 

class Config:
    API_ID = environ.get("API_ID", "22182189")
    API_HASH = environ.get("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5")
    BOT_TOKEN = environ.get("BOT_TOKEN", "70955...") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Takila0023:kilaogi06b90@cluster0.wzya1rw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7641464333').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
