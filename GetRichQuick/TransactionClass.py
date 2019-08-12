from .Stock import Stock

class Transaction:
    def __init__(self, transactionVolume, stockId, orderType):
        self.stock = Stock(stockId)
        pricetuple = self.stock.getCurrentStockPrice()
        self.transactionDate = pricetuple[0]
        self.transactionPrice = pricetuple[1]
        self.transactionVolume = transactionVolume
        self.orderType = orderType

    def __str__(self):
       return 'A ' + str(self.orderType) + " of " + str(self.stock.stockId) + " of size " + str(self.transactionVolume) + ' is executed on ' + str(self.transactionDate) + ' for the price of ' + str(self.transactionPrice)
#
##trans = Transaction(10,"ING","buy")
#print(trans)