import requests
import json, config.config as config

symbol = "XRPUSDT" # Replace with the symbol you want to get the trades for
limit = 500 # Maximum number of trades to retrieve per request
startTime = None # Unix timestamp in milliseconds, optional
endTime = None # Unix timestamp in milliseconds, optional

params = {"symbol": symbol
        , "limit": limit
        }
if startTime:
    params["startTime"] = startTime
if endTime:
    params["endTime"] = endTime
# add signature to params
params['signature'] = config.get_signature(params)
#  config.get_signature(params)

response = requests.get(config.API_URL_GET_TRADES, headers=config.API_HEADERS, params=params)
trades = json.loads(response.text)

print(trades)