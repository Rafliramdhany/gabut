#pip install cryptocompare
import cryptocompare

btc = cryptocompare.get_price('BTC')
print(btc)