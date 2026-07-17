from binance_client import get_price

def analyze():
    price = get_price()

    if price > 100000:
        signal = "SELL 🔴"
    else:
        signal = "BUY 🟢"

    return f"""
🤖 AI Trading Analysis

💰 BTC Price: {price}

📊 Signal: {signal}
"""
