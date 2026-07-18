import requests

def get_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    return float(data["price"])
