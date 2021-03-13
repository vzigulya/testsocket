from flask import Flask, url_for, render_template
import config, csv, json
from binance.client import Client

# url_for('static', filename='chart.js')
# url_for('static', filename='favicon.ico')
app = Flask(__name__)


client = Client(config.API_KEY, config.API_SECRET)


# ROUTES
@app.route('/')
def index():
    title = 'Coin View'
    info = client.get_account()
    balances = info['balances']
    print (balances)
    return render_template('test.html', title=title, my_balances = balances)

@app.route('/buy')
def buy():
    return 'Buy'

@app.route('/sell')
def sell():
    return 'Sell'    

@app.route('/settings')
def settings():
    return 'Settings'       