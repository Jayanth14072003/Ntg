import asyncio
from pyrogram import Client, compose,idle
import os
from config import Config
from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5377834462:AAFr_4q9Sw3RtGPoMtgkxy-w4A6TE8oN_0w")

API_ID = int(os.environ.get("API_ID", "13384432"))

API_HASH = os.environ.get("API_HASH", "ea9db4503ed7088b788e06dfd818e00e")

STRING = "Config.STRING_SESSION"


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
