import requests as rq
import matplotlib.pylab as plt
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


def get_exchange_rates(base: str, symbol: str, start_date: str, finish_date: str) -> (list, list):
    exchange_rates_api_url = f"""https://api.exchangeratesapi.io/history?start_at={start_date}&end_at={finish_date}&base={base}&symbols={symbol}"""
    try:
        response = rq.get(exchange_rates_api_url)
        rates: dict = response.json()['rates']
        lists = sorted(rates.items())  # sorted by key, return a list of tuples
        x, tuple_y = zip(*lists)  # unpack a list of pairs into two tuples
        list_of_dict = list(tuple_y)
        y = []
        for i in range(0, len(list_of_dict)):
            y.append(list_of_dict[i][symbol])
        return x, y
    except(ConnectionError, Timeout, TooManyRedirects) as e:
        print(f'Exception has occurred : {e}')


def plot_exchange_rates(base: str, symbol: str, start_date: str, finish_date: str):
    plt.plot(*get_exchange_rates(base, symbol, start_date, finish_date))
    plt.xlabel('Time')
    plt.ylabel(f'{base} to {symbol}')
    plt.title(f'Value of {base} in {symbol}. Time period : {start_date} : {finish_date}')
    plt.show()





