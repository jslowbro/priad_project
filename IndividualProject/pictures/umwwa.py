import requests as rq
from requests import Timeout, TooManyRedirects
import configparser


def um_kultura():
    config = configparser.ConfigParser()
    config.read('config.ini')
    key = config['umwwa.api.key']['key']
    url = f"""https://api.um.warszawa.pl/api/action/wmsstore_get/?id=374b1b7d-feba-40ab-ae22-2417
    354e61a0&format=png&apikey={key}"""
    try:
        response = rq.get(url)
        results = response.json()
        print(results)

        return results[0]['bounds']['northeast'], results[0]['bounds']['southwest']
    except(ConnectionError, Timeout, TooManyRedirects) as e:
        print(f'Exception has occurred : {e}')



um_kultura()