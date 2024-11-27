'''
1. Client should be having support for data streaming [websockets]
2. holdings, orders, trades, balance, order_status, , should be able to get this information (through websocket or webhook if available) [websockets if available]
3. place_order, cancel_order, modify_order, historical data [REST API's]
4. Should be able to handle Testnet, Mainnet, Futures, Spot, Margin
5. Async everywhere
6. Never have changing data in class variables
7. use Pydantics for data validation

Today's task:
    - Complete the binance broker class and testing
'''

from broker.constants.broker import Broker

class BinanceBroker:
    API_URL = 'https://api{}.binance.{}/api'
    API_TESTNET_URL = 'https://testnet.binance.vision/api'
    MARGIN_API_URL = 'https://api{}.binance.{}/sapi'
    FUTURES_URL = 'https://fapi.binance.{}/fapi'
    FUTURES_TESTNET_URL = 'https://testnet.binancefuture.com/fapi'
    FUTURES_DATA_URL = 'https://fapi.binance.{}/futures/data'
    FUTURES_DATA_TESTNET_URL = 'https://testnet.binancefuture.com/futures/data'
    TIME_FRAMES = {
        '1m': '1m',
        '5m': '5m',
        '15m': '15m',
        '30m': '30m',
        '1h': '1h',
        '4h': '4h',
        '1d': '1d',
        '1w': '1w',
        '1M': '1M'
    }
    ORDER_STATUS = {
        'NEW': 'NEW',
        'PARTIALLY_FILLED': 'PARTIALLY_FILLED',
        'FILLED': 'FILLED',
        'CANCELED': 'CANCELED',
        'PENDING_CANCEL': 'PENDING_CANCEL',
        'REJECTED': 'REJECTED',
        'EXPIRED': 'EXPIRED'
    }
    ROUTES = {
        Broker.REST_CREATE_ORDER: '',
        Broker.REST_GET_ORDER_STATUS: '',
        Broker.REST_GET_ORDER_BOOK: '',
        Broker.REST_GET_TRADES_BOOK: '',
        Broker.REST_GET_HOLDINGS: '',
        Broker.REST_CANCEL_ORDER: '',
        Broker.REST_UPDATE_ORDER: '',
        Broker.REST_GET_LTP_PRICE: '',
        Broker.REST_GET_DEPTH: '',
        Broker.REST_GET_KLINES: '',
        Broker.REST_GET_PRICE_QUANTITY_PRECISION: '',
        Broker.REST_SET_LEVERAGE: '',
        Broker.REST_SET_MARGIN_MODE: '',
        Broker.REST_GET_USER_DATA: '',
    }


    def __init__(self, api_key, api_secret):
        pass