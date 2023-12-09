import os

class Config(object):
    LOGGER = True

"""
Things to be noted you can fill values between empty "" 
Example - JOIN_LOGGER = os.environ.get("EVENT_LOGS", "-100828822882")

• If value is none there add "" to fill if you don't wanna fill add None

• Some vars are already filled to help you no need to change them.
"""


# Token from botfather 
TOKEN = os.environ.get("TOKEN", "6491531689:AAFaxNvZyiyPE8lhZlo2dNv45yZoHVjSSIQ")

# Make a new group then add @ScenarioXbot then send /id and fill id here.
JOIN_LOGGER = os.environ.get("EVENT_LOGS", "-1001603027566")

# only one # don't remove other one.
OWNER_ID = int(os.environ.get("OWNER_ID", "1556830659")) 

# only one # don't remove other one.
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "lochakpochak")

# can add multiple with spaces
DRAGONS = {int(x) for x in os.environ.get("DRAGONS", "6088155585").split()}

# can add multiple with spaces
DEV_USERS = {int(x) for x in os.environ.get("DEV_USERS", "6088155585").split()}

# can add multiple with spaces
DEMONS = {int(x) for x in os.environ.get("DEMONS", "6088155585").split()} 

# can add multiple with spaces
WOLVES = {int(x) for x in os.environ.get("WOLVES", "").split()}

# can add multiple with spaces
TIGERS = {int(x) for x in os.environ.get("TIGERS", "").split()}

# Should I show profile pic of user in /info command? 
# default value is true
INFOPIC = bool(os.environ.get("INFOPIC", True)) or "https://telegra.ph/file/a9ec99487ecd550460309.jpg"

# Make a new group then add @ScenarioXbot then send /id and fill id here.
EVENT_LOGS = os.environ.get("EVENT_LOGS", "-1001603027566")

# Make a new group then add @ScenarioXbot then send /id and fill id here.
ERROR_LOGS = os.environ.get("ERROR_LOGS", "-1001603027566")

# Don't touch if you don't know.
WEBHOOK = bool(os.environ.get("WEBHOOK", False))

# heroku app url
URL = os.environ.get("URL", "")  # If You Deploy On Heroku. [URL PERTEN:- https://{appname}.herokuapp.com/ || EXP:- https://scenario.herokuapp.com/]
PORT = int(os.environ.get("PORT", 8443))

CERT_PATH = os.environ.get("CERT_PATH")

# Bot Owner's API_ID (From:- https://my.telegram.org/apps)
API_ID = os.environ.get("API_ID", "23653093")

# Bot Owner's API_HASH (From:- https://my.telegram.org/apps)
API_HASH = os.environ.get("API_HASH", "ee6df88753c36eeab95391940ba3844f")

# Any SQL Database Link (RECOMMENDED:- PostgreSQL & https://www.elephantsql.com)
DB_URL = os.environ.get("DATABASE_URL", "postgres://joestroq:xFuhuUu_XRrZA-KzUkCNLWVq14qT4yIu@isabelle.db.elephantsql.com/joestroq") 

# Don't touch
DB_URL = DB_URL.replace(
"postgres://", "postgresql://", 1
)  # rest of connection code using the connection string `uri`

# Donation Link (ANY)
DONATION_LINK = os.environ.get("https://t.me/lochakpochak")

# Wall api key for wallpapers # From:- https://wall.alphacoders.com/api.php
WALL_API = os.environ.get("WALL_API", None) 

# To remove background of images # From:- https://www.remove.bg/
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", "")

## More info written at right side from this line.

OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", "") # From:- https://openweathermap.org/api
GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN", None) # From:- http://genius.com/api-clients
MONGO_DB_URL = os.environ.get("MONGO_DB_URL", "mongodb+srv://Cluster006:600510@cluster006.ootpa.mongodb.net/Cluster006?retryWrites=true&w=majority")
REDIS_URL = os.environ.get("REDIS_URL", "redis://Madharjoot:GuKhao123_@redis-12276.c275.us-east-1-4.ec2.cloud.redislabs.com:12276/Madharjoot")
BOT_ID = int(os.environ.get("BOT_ID", 6491531689)) # Telegram Bot ID (EXP:- 1241223850)
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", None) # Support Chat Group Link (Use @ScenarioXSupport || Dont Use https://t.me/ScenarioXSupport)
SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None) # Use @SpamWatchSupport
SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None) # From https://t.me/SpamWatchBot 
BOT_USERNAME = os.environ.get("BOT_USERNAME", "Tessa_Ro_bot") # Bot Username

STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIwBu5tshZMHbtj0ifWhcrHggvWzjyW1UPH9NVMdv-f4d43coEbQ_RdB9DF4g1Wf8kVGZ2t7cWd1V86EwzL4wP5G0CdZb3GqpYFpUk08koJH01AMihEtBB89VgNXPR7_432wdQmbN-RR5OlZJ-d93M9-ifGxzaQyHVZN43wVr9KZv2z-vQA7T2v4a-2A2D2442gMlRJ1gJJJ-6W7Jxc06kUm3d_f8BOGL34ms8dcCmg82DkbeqY2dvFutqoOYQHDZR3682I_BExkl1ELDIZZmb2wr2EUNJZq7IUL1-p9bRCZX1Iad44Vssi0A-JicNyLz8D2X54eo3a_gU36myIzNeL1G1A=") # Telethon Based String Session (2nd ID) [ From https://repl.it/@SpEcHiDe/GenerateStringSession ]
REPO = "TeamScenario/Scenario"
DEVELOPER = "lochakpochak"
APP_ID = API_ID
APP_HASH = API_HASH
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", True) # Heroku App Name 
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", True) # Heroku API [From https://dashboard.heroku.com/account]
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", True)
UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", True)
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", True)
ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True) # Don't Change
BOT_NAME = os.environ.get("BOT_NAME", True) # Name Of your Bot.
MONGO_DB = "scenario" # Don't change else errors.
ARQ_API_URL = "https://arq.hamker.in"
GOOGLE_CHROME_BIN = "/usr/bin/google-chrome"
CHROME_DRIVER = "/usr/bin/chromedriver"
SUDO_USERS = "2142595466"
WHITELIST_USERS = "2142595466"
BOT_API_URL = os.environ.get('BOT_API_URL', "https://api.telegram.org/bot")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "TeamScenario")

HELP_IMG = os.environ.get("HELP_IMG", True) or "https://telegra.ph/file/a9ec99487ecd550460309.jpg"
GROUP_START_IMG = os.environ.get("GROUP_START_IMG", True) or "https://telegra.ph/file/a9ec99487ecd550460309.jpg"
scenario_pic = os.environ.get("scenario_pic", True) or "https://telegra.ph/file/a9ec99487ecd550460309.jpg"

BL_CHATS = {int(x) for x in os.environ.get("BL_CHATS", "").split()}


# Don't Change
LOAD = os.environ.get("LOAD", "").split() 

# Don't Change
NO_LOAD = os.environ.get("NO_LOAD", "translation").split()

# Don't Change
DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))

# Don't Change
STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False)) or "True"

# Don't Change
WORKERS = int(os.environ.get("WORKERS", 8))

# Sticker id here if you want to ban any
BAN_STICKER = os.environ.get("BAN_STICKER", "")

# Don't Change
ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)

# Don't Change
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")

# Already filled no need to fill again.
CASH_API_KEY = os.environ.get("CASH_API_KEY", None) or "70F3DVSKF6RUAHQV"

# Already filled no need to fill again.
TIME_API_KEY = os.environ.get("TIME_API_KEY", None) or "K5PTMFOEC82M"

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
