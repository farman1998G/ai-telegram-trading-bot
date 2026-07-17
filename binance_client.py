from binance.client import Client
import os

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

client = Client(API_KEY, API_SECRET)

def get_price(symbol="BTCUSDT"):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker["price"])
