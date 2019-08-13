from .Stock import Stock
from .Position import Position


class Portfolio:
    positions = list()

    def AddPosition(self, stockId, transactionVolume):
        for position in self.positions:
            if position.stock.stockId == stockId:
                position.updatePosition(transactionVolume)
                return

        self.positions.append(Position(Stock(stockId), transactionVolume))

    def GetPortfolioValue(self):
        value = 0
        for position in self.positions:
            value += position.volume * float(position.stock.getCurrentStockPrice()[1])
        return value