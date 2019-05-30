from IndividualProject.finance import currency_market as cm
from IndividualProject.finance import cryptocurrency_market as crypto
from random import randint

cm.plot_exchange_rates('EUR', 'USD', '2017-01-01', '2019-01-01')
print('*****DATA ABOUT A SINGLE CRYPTO-CURRENCY******\n\n')
print(f"{crypto.coin_data('BTC', 'USD')}\n\n")
print('****LIST OF ATTRIBUTES BY WHICH YOU SORT COINS BY*****\n\n')
print(f'{crypto.attributes}\n\n')
attribute = crypto.attributes[randint(0, len(crypto.attributes)-1)]
print(f'*****LIST OF CURRENCIES SORTED BY {attribute}******\n\n')
print(crypto.coins_sorted_by('percent_change_1h', 'USD', 100))


