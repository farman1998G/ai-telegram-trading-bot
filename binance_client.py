import requests

def get_price(symbol="BTCUSDT"):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    return float(data["bitcoin"]["usd"])
