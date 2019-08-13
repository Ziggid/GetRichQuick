from .Stock import Stock
from .user import User
from peewee import *
db = SqliteDatabase('getrich.db')


class Portfolio(Model):
    # positions = list() needs to be backreffed
    user = ForeignKeyField(User, backref='portfolios')

    # def add(self, position):
    #     self.positions.append(position)

    def addPosition(self, stockId, transactionVolume):
        for position in self.positions:
            if position.stock.stockId == stockId:
                position.updatePosition(transactionVolume)
                return
        s = Stock(stockId=stockId)
        p = Position(volume=transactionVolume, portfolio = self, stock = s)
        # self.positions.append(Position(Stock(stockId), transactionVolume))

    def GetPortfolioValue(self):
        value = 0
        for position in self.positions:
            value += position.volume * float(position.stock.getCurrentStockPrice()[1])
        return value

    class Meta:
        database = db


class Position(Model):
    # def __init__(self, stock, volume):
    #     self.stock = stock
    #     self.volume = volume..
    volume = FloatField()
    portfolio = ForeignKeyField(Portfolio, backref='positions')
    stock = ForeignKeyField(Stock, backref='positions')
    def updatePosition(self, volume):
        if self.volume + volume < 0:
            print('Negative position not allowed')
        else:
            self.volume += volume

    class Meta:
        database = db