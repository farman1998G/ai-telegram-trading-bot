import os
import asyncio
from telegram import Bot
from ai_analysis import analyze

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def start_bot():
    bot = Bot(token=TOKEN)

    while True:
        message = analyze()

        await bot.send_message(
            chat_id=CHAT_ID,
            text=message
        )

        await asyncio.sleep(300)
