from pycoingecko import CoinGeckoAPI


def get_currencies():
    currencies = [
        ('BTC', 'BTC'),
        ('UAH', 'UAH'),
        ('ETH', 'ETH'),
        ('USD', 'USD'),
        ('BNB', 'BNB'),
        ('LTC', 'LTC'),
        ('XRP', 'XRP'),
        ('BCH', 'BCH'),
        ('EOS', 'EOS'),
    ]
    return currencies


def translate_crypto(crypto):
    cur = {
        'BTC': 'bitcoin',
        'UAH': 'uah',
        'ETH': 'ethereum',
        'USD': 'tether',
        'BNB': 'binancecoin',
        'LTC': 'binance-peg-litecoin',
        'XRP': 'binance-peg-xrp',
        'BCH': 'binance-peg-bitcoin-cash',
        'EOS': 'binance-peg-eos'
    }
    return cur[crypto]


cg = CoinGeckoAPI()


def get_price(amount, give, take):
    if give == 'uah':
        take = translate_crypto(take.upper())
        price = cg.get_price(ids=take, vs_currencies=give)[take][give]
        price = float(amount) * (1/price)
        return price
    price = cg.get_price(ids=give, vs_currencies=take)[give][take]
    price = price * float(amount)
    print(price)
    return price
