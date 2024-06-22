from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "1993"))
    API_HASH = getenv("API_HASH", "6a6df8006d3056d37baca")
    BOT_TOKEN = getenv("BOT_TOKEN", "6991yEWC9bNRAZlLl939UciJeMJO8C0Vbs")
    FSUB = getenv("FSUB", "https://t.me/+P-wgdlU3MTM1")
    CHID = int(getenv("CHID", "-100182305"))
    SUDO = int(getenv("SUDO", "6331874"))
    MONGO_URI = getenv("MONGO_URI", "mongodb+3.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
