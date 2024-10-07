import time
from broker.base_broker import BaseBroker
import dotenv
import os
dotenv.load_dotenv()

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

class BinanceBroker(BaseBroker):
    """
    BinanceBroker class implements the broker interface for Binance.
    Extends BaseBroker to provide specific functionality for Binance API.
    """

    def __init__(self, api_key, api_secret):
        super().__init__()
        try:
            self.client = Client(api_key, api_secret)
        except:
            raise ValueError("Invalid API key or secret")

    def get_historical_data(self, symbol = 'BTCUSDT', interval='1h', start_time=None, end_time=None):
        if start_time is None:
            start_time = int(time.time() * 1000) - 86400000
        if end_time is None:
            end_time = int(time.time() * 1000)
        return self.client.get_historical_klines(symbol, interval, start_time, end_time)

    def get_live_data(self, symbol):
        """
        Fetches live price data for a symbol.
        :param symbol: Trading symbol (e.g., 'BTCUSDT')
        """
        return self.client.get_orderbook_ticker(symbol)

    def _get_headers(self):
        return {}

    def get_account_info(self):
        return None

    def place_order(self, symbol, side, quantity, price=None):
        return None

    def get_order_status(self, order_id, symbol):
        return None

    def get_live_positions(self):
        return None

if __name__ == "__main__":
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    broker = BinanceBroker(api_key, api_secret)
    
    symbol = "BTCUSDT"
    interval = "1h"
    start_time = int(time.time() * 1000) - 86400000
    end_time = int(time.time() * 1000)
    historical_data = broker.get_historical_data(symbol, interval, start_time, end_time)
    print("Historical Data:", historical_data)