from .Stock import Stock
from .Position import Position


class Portfolio:
    positions = list()

    def AddPosition(self, stockId, transactionVolume):
        for position in self.positions:
            if position.stock.stockId == stockId:
                position.updatePosition(transactionVolume)
                return

        if transactionVolume >= 0:
            self.positions.append(Position(Stock(stockId), transactionVolume))
        else:
            print('Negative position not allowed. Transaction of ' + str(transactionVolume) + ' ' + str(stockId) + ' stocks was denied.')

    def GetPortfolioValue(self):
        value = 0
        for position in self.positions:
            value += position.volume * float(position.stock.getCurrentStockPrice()[1])
        return value