import configparser
import requests as rq
from requests import Timeout, TooManyRedirects


def get_lat_len(street, city, printable=False):
    config = configparser.ConfigParser()
    config.read('config.ini')
    key = config['opencage.api.key']['key']
    url = f"https://api.opencagedata.com/geocode/v1/json?q={street}%2C%20{city}&key={key}&language=en&pretty=1"
    try:
        response = rq.get(url)
        results = response.json()['results']
        if printable:
            print(results)

        return results[0]['bounds']['northeast'], results[0]['bounds']['southwest']
    except(ConnectionError, Timeout, TooManyRedirects) as e:
        print(f'Exception has occurred : {e}')


def get_formatted_adress(lat, len):
    config = configparser.ConfigParser()
    config.read('config.ini')
    key = config['opencage.api.key']['key']
    url = f"https://api.opencagedata.com/geocode/v1/json?q={lat}%2C%20{len}&key={key}&language=en&pretty=1"
    try:
        response = rq.get(url)
        results = response.json()['results']
        return results[0]['formatted']
    except(ConnectionError, Timeout, TooManyRedirects) as e:
        print(f'Exception has occurred : {e}')


print(get_lat_len('Kompasowa', 'Warszawa'))
print(get_formatted_adress(31.79261, 35.21785))