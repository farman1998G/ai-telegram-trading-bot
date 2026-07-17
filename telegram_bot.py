from telegram import Bot
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = Bot(token=TOKEN)

def start_bot():
    bot.send_message(
        chat_id=CHAT_ID,
        text="🤖 AI Trading Bot uğurla başladı!"
    )
