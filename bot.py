import pyrogram
from pyrogram import Client, filters
import tgcrypto
from details import api_id, api_hash, bot_token

bot = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@bot.on_message(filters.command("start") & filters.private)

def welcome(client,message): 
    message.reply_text(text="Hello")

@bot.on_message(filters.text & filters.private)
def echo(Client,message):
 message.reply_text(text=message.text)

 bot.run()
