class Stock:

    def __init__(self, stockId,  date):
        self.stockId = stockId
        self.date = date

    def getStockPrice(self, stockId, date):
         return "hoi"

    def __str__(self):
        return 'The stock ' + str(self.stockId) + ' trades for ...' + ' on ' + str(self.date)