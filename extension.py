import json
import requests
from config import keys

class ConvertionExceprion(Exception):
    pass

class CriptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str, ):
        if quote == base:
            raise ConvertionExceprion('невозможно конвертировать в одинаковые валюты')

        try:
            quote_ticker = keys[quote]
        except keyError:
            raise ConvertionExceprion(f'введена неправильная или несуществующая валюта {quote}')

        try:
            base_ticker = keys[base]
        except keyError:
            raise ConvertionExceprion(f'введена неправильная или несуществующая валюта {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExceprion(f'введено неправильное количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return (total_base * amount)