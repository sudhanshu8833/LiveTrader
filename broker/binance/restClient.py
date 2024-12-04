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
import hmac
import hashlib
import requests
import binance
import aiohttp
from broker.constants.broker import BrokerConstants

class BinanceBroker:
    API_URL = 'https://api.binance.com/api/v3'
    API_TESTNET_URL = 'https://testnet.binance.vision/api/v3'
    FUTURES_URL = 'https://fapi.binance.com/fapi/v1'
    FUTURES_TESTNET_URL = 'https://testnet.binancefuture.com/fapi/v1'


    TIME_FRAMES = {
        BrokerConstants.TIMEFRAME_1m: '1m',
        BrokerConstants.TIMEFRAME_5m: '5m',
        BrokerConstants.TIMEFRAME_15m: '15m',
        BrokerConstants.TIMEFRAME_30m: '30m',
        BrokerConstants.TIMEFRAME_1H: '1h',
        BrokerConstants.TIMEFRAME_4H: '4h',
        BrokerConstants.TIMEFRAME_1D: '1d',
        BrokerConstants.TIMEFRAME_1W: '1w',
        BrokerConstants.TIMEFRAME_1M: '1M'
    }

    ORDER_STATUS = {
        BrokerConstants.STATUS_OPEN: 'NEW',
        BrokerConstants.STATUS_PARTIALLY_FILLED: 'PARTIALLY_FILLED',
        BrokerConstants.STATUS_FILLED: 'FILLED',
        BrokerConstants.STATUS_CANCELLED: 'CANCELED',
        BrokerConstants.STATUS_CANCELLED: 'REJECTED',
        BrokerConstants.STATUS_CANCELLED: 'EXPIRED'
    }

    ROUTES = {
        BrokerConstants.REST_CREATE_ORDER: '/order',
        BrokerConstants.REST_CREATE_OCO_ORDER: '/orderList/oco',
        BrokerConstants.REST_GET_ORDER_STATUS: '/order',
        BrokerConstants.REST_GET_ORDER_BOOK: '/allOrders',
        BrokerConstants.REST_GET_TRADES_BOOK: '',
        BrokerConstants.REST_GET_HOLDINGS: '',
        BrokerConstants.REST_CANCEL_ORDER: '/order',
        BrokerConstants.REST_UPDATE_ORDER: '',
        BrokerConstants.REST_GET_LTP_PRICE: '/ticker/price',
        BrokerConstants.REST_GET_DEPTH: '/depth',
        BrokerConstants.REST_GET_KLINES: '/klines',
        BrokerConstants.GET_EXCHANGE_INFO: '/exchangeInfo',
        BrokerConstants.REST_SET_LEVERAGE: '/leverage',
        BrokerConstants.REST_SET_MARGIN_MODE: '/marginType',
        BrokerConstants.REST_GET_ACCOUNT_INFO: '/account',
    }

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def _get_signature(self, payload):
        return hmac.new(self.api_secret.encode('utf-8'),payload.encode('utf-8'),hashlib.sha256).hexdigest()

    def _get_header(self):
        return {
            'X-MBX-APIKEY': self.api_key,
            'content-type': 'application/x-www-form-urlencoded'
        }
    
    async def _request(self, method, route, params = None, payload = None):
        url = self.BASE_URL + route
        headers = self._get_headers()

        if params:
            query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
            signature = self._get_signature(query_string)
            query_string += f"&signature={signature}"

        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, headers=headers, data=payload) as response:
                if response.status != 200:
                    response_text = await response.text()
                    raise Exception(f"Error {response.status}: {response_text}")
                return await response.json()

    
    async def create_order(self, payload):
        route = self.ROUTES[BrokerConstants.REST_CREATE_ORDER]
        return await self._request(BrokerConstants.POST, route, payload=payload)