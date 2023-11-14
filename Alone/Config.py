#MIT License
#Copyright (c) 2023, ©AloneXBots

import sys
from logging import getLogger

LOGGER = getLogger(__name__)

# Required ENV
try:
    BOT_TOKEN = "" # BOT TOKEN
    API_ID =  123 # API ID
    API_HASH = "" # API HASH
except Exception as e:
    LOGGER.error(f"Looks Like Something Is Missing!! Please Check Variables\n{e}")
    sys.exit(1)


TIMEZONE = "Asia/Kolkata" # YOUR TIME ZONE

COMMAND_HANDLER = ". /".split() # COMMAND HANDLER

SUDO = list({int(x)for x in ("").split()})

SUPPORT_CHAT = "AlonesHeaven" # SUPPORT GROUP (ID OR USERNAME)

LOG_CHANNEL_ID = -1001603822916 #LOG GROUP ID FOR YOUR BOT

OWNER = list({int(x)for x in ("6079943111").split()}) #OWNER ID

DB_URL = "" # MONGO DB URL

SQL_URL = "" # ELEPHANT SQL URL
