class Transaction:
    def __init__(self, transactionDate, transactionVolume, transactionPrice, stockId, orderType):
        self.transactionDate = transactionDate
        self.transactionVolume = transactionVolume
        self.transactionPrice = transactionPrice
        self.stockId = stockId
        self.orderType = orderType

    #def __str__(self):
        #'A' + self.orderType + "of" + self.stockId + "of size" + self.transactionVolume + 'is executed on' self.transactionDate + 'for the price of' + self.transactionPrice

