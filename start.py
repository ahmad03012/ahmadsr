import pyrogram
from pyrogram import filters
import config

app = pyrogram.Client(
    ":deblo:",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

@app.on_message(filters.command("start"))
async def start_command(_, message: m):
    await m.reply("Hallo deblo")
    

app.run()
