from urllib.parse import urlencode
import config, csv, hashlib, time,datetime,  requests, json,urllib3,  urllib, json
from binance.client import Client

# signature = 'mySecretWord'
# hashedsig = hashlib.sha256(str(signature).encode('utf-8')).hexdigest()
# servertime = requests.get("https://api.binance.com/api/v1/time")
# servertimeobject = json.loads(servertime.text)
# servertimeint = servertimeobject['serverTime']

# request_params = {
#     "signature" : hashedsig,
#     "timestamp" : servertimeint,
# }

# request_params = dict([('signature')])

client = Client(config.API_KEY, config.API_SECRET)
client.API_URL = "https://testnet.binance.vision/api"
# balance = client.get_account()
# balance =  client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")
# /api/v3/account
# for bal in balance:
#     print(bal)

symbol = "XRPUSDT" # Replace with the symbol you want to get the trades for
limit = 500 # Maximum number of trades to retrieve per request
startTime = None # Unix timestamp in milliseconds, optional
endTime = None # Unix timestamp in milliseconds, optional

# _date = datetime.datetime.timestamp
_trades_params1 = {"symbol":symbol}
params = {"symbol": symbol, "limit": limit}
_trades = client.get_my_trades(symbol=symbol, limit=limit)
# print(_date)
print(_trades)

timestamp = datetime.datetime.now()
print('timestamp:', timestamp)
print(time.mktime(datetime.datetime.now().timetuple()))