class Transaction:
    def __init__(self, transactionDate, transactionVolume, transactionPrice, stockId, orderType):
        self.transactionDate = transactionDate
        self.transactionVolume = transactionVolume
        self.transactionPrice = transactionPrice
        self.stockId = stockId
        self.orderType = orderType

    def __str__(self):
        return 'A ' + str(self.orderType) + " of " + str(self.stockId) + " of size " + str(self.transactionVolume) + ' is executed on ' + str(self.transactionDate) + ' for the price of ' + str(self.transactionPrice)