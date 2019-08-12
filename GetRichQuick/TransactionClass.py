class Transaction:
    def _init_(self, transactionDate, transactionVolume, transactionPrice, stockId, orderType ):
        self.transactionDate = transactionDate
        self.transactionVolume = transactionVolume
        self.transactionPrice = transactionPrice
        self.stockId = stockId
        self.orderType = orderType

    def _str_(self):
        return 'A' + self.orderType + "of" + self.stockId + "of size" + self.transactionVolume + 'is executed on' self.transactionDate + 'for the price of' + self.transactionPrice

