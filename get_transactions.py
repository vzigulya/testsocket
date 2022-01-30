from urllib.parse import urlencode
import config, csv, hashlib, time,  requests, json,urllib3,  urllib
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
print(client.get_my_trades())