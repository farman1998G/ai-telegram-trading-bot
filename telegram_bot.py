from telegram import Bot
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def start_bot():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    import asyncio

    async def send():
        await bot.send_message(
            chat_id=TELEGRAM_CHAT_ID,
            text="🤖 AI Trading Bot uğurla başladı!"
        )

    asyncio.run(send())
