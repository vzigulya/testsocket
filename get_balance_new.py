import csv, hashlib, time, requests, json,urllib3, urllib3, urllib
from binance.client import Client

api_key = "aBzSFRrFu6Oe1jcSJqRXWToFYQ3EKGPKZ9f5BXH9u5x8n7WfkSXTwePZo9sXikwt"
api_secret = "M88hUgkmzGn7pCGqS5Y5ULCCtkbQjmwEU7PCMphTbbjd0xbU6mPKups4IvANJNDF"

client = Client(api_key, api_secret)
client.API_URL = "https://testnet.binance.vision/api"

print(client.get_account())