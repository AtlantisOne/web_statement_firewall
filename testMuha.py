# Модуль получения данных с API и запись в базу данных.

"""
curl -H "X-CMC_PRO_API_KEY: d61bca4c-e9d3-40b9-8d82-abf9b057ffbd"
-H "Accept: application/json" -d "id=1"
-G https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest
"""

import requests
# from django.core import serializers

def response():
    response = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest', headers={
        'X-CMC_PRO_API_KEY': 'd61bca4c-e9d3-40b9-8d82-abf9b057ffbd',
        'Accept': 'application/json',
    }, params=(('id', '1'),))
    return response.json()

def serialize_response(data):
    return {
        'name': data['data']['1']['name'],
        'date_added': data['data']['1']["date_added"],
        'last_updated': data['data']['1']["last_updated"],
        'price': data['data']['1']["quote"]["USD"]["price"],
        'volume_24h': data['data']['1']["quote"]["USD"]["volume_24h"],
        'percent_change_24h': data['data']['1']["quote"]["USD"]["percent_change_24h"]
    }

print(serialize_response(response()))