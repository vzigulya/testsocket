from sqlite3 import Time, Timestamp
import config, csv, hashlib, time,  requests, json,urllib3,  urllib
from binance.client import Client


client = Client(config.API_KEY, config.API_SECRET)
client.API_URL = config.API_URL



bal = client.get_account()
    # JSON example
    # {'makerCommission': 0, 'takerCommission': 0, 'buyerCommission': 0, 'sellerCommission': 0
    # , 'canTrade': True, 'canWithdraw': False, 'canDeposit': False, 'updateTime': 1642978832225, 
    # 'accountType': 'SPOT'
    # , 'balances': [
        #   {'asset': 'BNB', 'free': '1000.00000000', 'locked': '0.00000000'}
        # , {'asset': 'BTC', 'free': '1.00000000', 'locked': '0.00000000'}
        # , {'asset': 'BUSD', 'free# ': '10000.00000000', 'locked': '0.00000000'}
        # , {'asset': 'ETH', 'free': '100.00000000', 'locked': '0.00000000'}
        # , {'asset': 'LTC', 'free': '500.00000000', 'locked': '0.00000000'}
        # , {'asset# ': 'TRX', 'free': '500000.00000000', 'locked': '0.00000000'}
        # , {'asset': 'USDT', 'free': '10000.00000000', 'locked': '0.00000000'}
        # , {'asset': 'XRP', 'free': '50000.00000000', 'locked': '0.00000000'}]
    # , 'permissions': ['SPOT']}
for x in bal['balances']:
    myasset =  x['asset']
    myasset_locked = x['locked']
    mysymbol = myasset+'USDT'
    mysymbol_info = client.get_symbol_info(mysymbol)
    myasset_exception = ['BUSD','USDT']
    # print(myasset)
    # should we use client.get_symbol_ticker
    if myasset not  in myasset_exception : mysymbol_avg_price = client.get_symbol_ticker(symbol=mysymbol)['price']
    # elif myasset != 'USDT': mysymbol_avg_price = client.get_avg_price(symbol=mysymbol)
    else: mysymbol_avg_price = 'Undefined'
    print(myasset,' ',x['free'], myasset_locked,mysymbol,mysymbol_avg_price)
        # {'mins': 5, 'price': '35910.98262412'}
    
    # print(symbol_info)
        # {'symbol': 'XRPUSDT', 'status': 'TRADING', 'baseAsset': 'XRP', 'baseAssetPrecision': 8, 'quoteAsset': 'USDT'
        # , 'quotePrecision': 8, 'quoteAssetPrecision': 8, 'baseCommissionPrecision': 8, 'quoteCommissionPrecision': 8
        # , 'orderTypes': ['LIMIT', 'LIMIT_MAKER', 'MARKET', 'STOP_LOSS_LIMIT', 'TAKE_PROFIT_LIMIT']
        # , 'icebergAllowed': True, 'ocoAllowed': True, 'quoteOrderQtyMarketAllowed': True
        # , 'isSpotTradingAllowed': True, 'isMarginTradingAllowed': False
        # , 'filters': [{'filterType': 'PRICE_FILTER', 'minPrice': '0.00010000', 'maxPrice': '1000.00000000', 'tickSize': '0.00010000'}
        # , {'filterType': 'PERCENT_PRICE', 'multiplierUp': '5', 'multiplierDown': '0.2', 'avgPriceMins': 5}
        # , {'filterType': 'LOT_SIZE', 'minQty': '0.10000000', 'maxQty': '90000.00000000', 'stepSize': '0.10000000'}git
        # , {'filterType': 'MIN_NOTIONAL', 'minNotional': '10.00000000', 'applyToMarket': True, 'avgPriceMins': 5}
        # , {'filterType': 'ICEBERG_PARTS', 'limit': 10}
        # , {'filterType': 'MARKET_LOT_SIZE', 'minQty': '0.00000000', 'maxQty': '10000.00000000', 'stepSize': '0.00000000'}
        # , {'filterType': 'MAX_NUM_ORDERS', 'maxNumOrders': 200}, {'filterType': 'MAX_NUM_ALGO_ORDERS', 'maxNumAlgoOrders': 5}]
        # , 'permissions': ['SPOT']}
   

# https://binance-docs.github.io/apidocs/spot/en/#new-order-trade
# buy_order_limit = client.create_order(
#      symbol='ETHUSDT',
#      side='BUY',
#      type='MARKET',
#      timestamp = Timestamp,
#      quantity=1)
# print(buy_order_limit)
# print(client.get_my_trades('BTCUSDT'))    

# print(client.get_symbol_ticker(symbol='BTCUSDT'))