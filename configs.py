from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "19937650"))
    API_HASH = getenv("API_HASH", "6a6df8006df3cb56edce33056d37baca")
    BOT_TOKEN = getenv("BOT_TOKEN", "6999160420:AAFD1yEWC9bNRAZlLl939UciJeMJO8C0Vbs")
    FSUB = getenv("FSUB", "https://t.me/+P-wgbt_2dlU3MTM1")
    CHID = int(getenv("CHID", "-1001802232305"))
    SUDO = int(getenv("SUDO", "6331847574"))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://strong:strong@cluster0.ix7usa3.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
