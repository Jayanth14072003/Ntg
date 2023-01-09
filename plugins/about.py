import os 
from pyrogram import Client, filters
from config import BOT_TOKEN
token = "BOT_TOKEN"
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["stats"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Tᴏᴛᴀʟ Usᴇʀ:- {total_user()}\nBᴏᴛ :- @KR_Renamer_Bot \n ᴄʀᴇᴀᴛᴇʀ :- @mrlokaman\nʟᴀɴɢᴜᴀɢᴇ :-ᴘʏᴛʜᴏɴ𝟹\n ʟɪʙʀᴀʀʏ :- ᴘʏʀᴏɢʀᴀᴍ 2.0\n sᴇʀᴠᴇʀ : - 𝙑𝙋𝙎 \n ᴛᴏᴛᴀʟ ʀᴇɴᴀᴍᴇᴅ ғɪʟᴇ :-{total_rename}\n ᴛᴏᴛᴀʟ sɪᴢᴇ ʀᴇɴᴀᴍᴇᴅ :- {humanbytes(int(total_size))} ",quote=True)
