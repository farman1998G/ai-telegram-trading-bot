import os
from openai import OpenAI
from binance_client import get_price

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze():
    price = get_price("BTCUSDT")

    prompt = f"""
You are a professional cryptocurrency analyst.

Current BTC price: {price} USD.

Analyze the market and answer in this format only:

Trend:
Signal:
Entry:
Take Profit:
Stop Loss:
Reason:
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return f"""🤖 AI Trading Analysis

💰 BTC Price: {price}

{response.choices[0].message.content}
"""
