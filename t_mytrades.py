import get_last_trades_by_symbol as trades
from datetime import datetime

# print ('XRPUSDT')
# t1 = trades.getTradesBySymbol('XRPUSDT',500)
# print(t1)

print ('ETHUSDT')
# orders = trades.getTradesBySymbol('ETHUSDT',500)
orders = [
    {'symbol': 'XRPUSDT', 'id': 318757, 'orderId': 3043247, 'orderListId': -1, 'price': '100', 'qty': '1', 'quoteQty': '0', 'commission': '0.00000000', 'commissionAsset': 'XRP', 'time': 1680226475450, 'isBuyer': True, 'isMaker': False, 'isBestMatch': True}
  , {'symbol': 'XRPUSDT', 'id': 319191, 'orderId': 3046346, 'orderListId': -1, 'price': '100', 'qty': '1', 'quoteQty': '0', 'commission': '0.00000000', 'commissionAsset': 'XRP', 'time': 1680228459815, 'isBuyer': True, 'isMaker': False, 'isBestMatch': True}
  , {'symbol': 'XRPUSDT', 'id': 319195, 'orderId': 3046379, 'orderListId': -1, 'price': '50', 'qty': '1', 'quoteQty': '0', 'commission': '0.00000000', 'commissionAsset': 'USDT', 'time': 1680228480721, 'isBuyer': False, 'isMaker': False, 'isBestMatch': True}
  , {'symbol': 'XRPUSDT', 'id': 340605, 'orderId': 3259553, 'orderListId': -1, 'price': '100', 'qty': '1', 'quoteQty': '0', 'commission': '0.00000000', 'commissionAsset': 'XRP', 'time': 1680343441374, 'isBuyer': True, 'isMaker': False, 'isBestMatch': True}]

# orders = client.get_my_trades(symbol='ETHUSDT')
overall = 0
accumulative_qty = 0
accumulative_net_price = 0
average_price = 0

print('ID', 'isBuyer', 'price', 'qty', 'Accumulative Net', 'AccumulativeQty')
for order in orders:
    ts = int(order['time']) / 1000
    dt = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    price = float(order['price'])
    qty = float(order['qty'])
    if order['isBuyer'] == True  : 
        order_type = 'BUY' 
        accumulative_qty += qty
        accumulative_net_price = accumulative_net_price + price*qty
    else:   
        order_type ='SELL'
        accumulative_qty -= qty
        accumulative_net_price = accumulative_net_price - price*qty
    average_price = accumulative_net_price/accumulative_qty

    print(
        dt
        , order['id']
        , order_type
        , order['price']
        , order['qty']
        , accumulative_net_price
        , accumulative_qty
        , average_price
        )
print('FINALLY')
print('accumulative_qty = ', accumulative_qty)
print('accumulative_net_price = ', accumulative_qty)
print('average_price = ', average_price)

