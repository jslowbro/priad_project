from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import matplotlib.pylab as plt
import numpy as np

attributes = [
    'name',
    'symbol',
    'slug',
    'circulating_supply',
    'total_supply',
    'date_added',
    'num_market_pairs',
    'platform',
    'cmc_rank',
    'last_updated',
    'price',
    'percent_change_1h',
    'percent_change_24h',
    'percent_change_7d',
    'market_cap',
]

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': 5000,
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '78fda70a-a1e5-4e18-861f-011308edbfcb',
}


def request_coin_data_json(convert):
    parameters.update({'convert': convert})
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        json_data = json.loads(response.text)['data']
        return json_data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def coin_data(coin_symbol, convert):
    data = request_coin_data_json(convert)
    for x in range(0, len(data)):
        if data[x]['symbol'] == coin_symbol:
            coin_index = x
    try:
        return data[coin_index]
    except NameError:
        print("You have entered an invalid coin name")


def coins_sorted_by(key, convert, no_coins):

    data = request_coin_data_json(convert)
    merged_data = merge_internal_dictionaries(data)
    try:
        new_list = sorted(merged_data, key=lambda k: k[key])
        return new_list[:no_coins]
    except TypeError as t:
        print('Wrong attribute')


def merge_internal_dictionaries(data):
    for x in data:
        internal_dict = x['quote']['USD']
        del x['quote']
        x.update(internal_dict)
    return data


def plot_exchange_rates(sorted_data, attribute, convert):
    attribute_list = []
    symbol_list = []
    for x in sorted_data:
        attribute_list.append(x[attribute])
        symbol_list.append(x['symbol'])
    plt.barh(symbol_list, attribute_list)
    plt.show()


plot_exchange_rates(coins_sorted_by('percent_change_1h', 'USD', 10), 'percent_change_1h', 'USD')