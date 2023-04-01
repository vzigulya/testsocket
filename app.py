from flask import Flask, url_for, render_template
import config.config as config, csv, json
import get_last_trades_by_symbol as trade_data
from binance.client import Client

# url_for('static', filename='chart.js')
# url_for('static', filename='favicon.ico')
app = Flask(__name__)


client = Client(config.API_KEY, config.API_SECRET)
client.API_URL = config.API_URL

# ROUTES
@app.route('/')
def index():
    title = 'Coin View'
    info = client.get_account()
    balances = info['balances']
    trade =  trade_data.getTradesBySymbol('ETHUSDT', 500)
    # print('tttttttt')
    # print (trade)
    return render_template('test.html', title=title, my_balances = balances, my_trades = trade)

@app.route('/buy')
def buy():
    return 'Buy'

@app.route('/sell')
def sell():
    return 'Sell'    

@app.route('/settings')
def settings():
    return 'Settings'       