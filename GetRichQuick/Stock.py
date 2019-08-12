class Stock

    def _init_(self, stockId,  date):
        self.stockId = stockId
        self.date = date



    def getStockPrice(self, stockId, date):
        return


    def _str_(self, stockId,  date):
        return 'The stock' + self.stockId + 'trades for ' + getStockPrice(stockId,  date) + 'on' + self.date