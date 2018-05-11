import ccxt
import pprint
import time

pp = pprint.PrettyPrinter()

class Exchange:
    def __init__(self):
        self.binance = ccxt.binance()
    def loadMarkets(self):
        self.binance.loadMarkets()
    def printExchanges(self):
        pp.pprint(ccxt.exchanges)
    def getAllTickers(self):
        return self.binance.fetch_tickers()

# # Market Price
# for i in range(0, len(exchange.symbols)):
#     orderbook = exchange.fetch_order_book(exchange.symbols[i])
#     bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
#     ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
#     spread = (ask - bid) if (bid and ask) else None
#     print (exchange.id, 'market price', { 'bid': bid, 'ask': ask, 'spread': spread })

# # Ticker Price
# for sym in exchange.symbols:
#     ticker = exchange.fetch_ticker(sym)
#     print(ticker['info']['lastPrice'])
