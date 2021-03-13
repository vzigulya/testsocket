import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

# prices = client.get_all_tickers()

# for price in prices:
	#  print(price)


# candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)
candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")
csvfile = open('15minutes.csv', 'w', newline='') 

candlestick_writer = csv.writer(csvfile, delimiter=',',)



for candlestick in candles:
	print(candlestick)
	candlestick_writer.writerow(candlestick)


csvfile.close()