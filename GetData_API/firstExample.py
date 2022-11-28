# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:22:58 2022

@author: ASUS
"""
import requests
apiKey = "8c59361d9d05e34d6047ef8ded4d83eb4af66a676abd6bffd3d557d01ea798a7"
crypto = "BTC"
header = 'fsym=' + str(crypto)
maxRecords = 100
frequency = "hour"
API_KEY = '&api_key=' + str(apiKey)
limit = '&limit=' + str(maxRecords)
currency = '&tsym=USD'
url = 'https://min-api.cryptocompare.com/data/v2/histo' + frequency + '?' + header + currency + API_KEY + limit
print(url)
response = requests.get(url).json()
print(response.keys())
# print(type(response['Data']))