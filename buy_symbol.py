from binance.client import Client
from sqlite3 import Time, Timestamp
import config

client = Client(config.API_KEY, config.API_SECRET)
client.API_URL = config.API_URL


# https://binance-docs.github.io/apidocs/spot/en/#new-order-trade
buy_order_limit = client.create_order(
     symbol='XRPUSDT',
     side='BUY',
     type='MARKET',
     timestamp = Timestamp,
     quantity=30
     )
print(buy_order_limit)