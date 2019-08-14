from .Stock import getCurrentStockPrice
from .user import User
from peewee import *

db = SqliteDatabase('getrich.db')


class Portfolio(Model):
    # positions = list() needs to be backreffed
    _user = ForeignKeyField(User, backref='portfolio')

    # def add(self, position):
    #     self.positions.append(position)

    def addPosition(self, stockId, transactionVolume):
        for position in self.positions:
            if position.stockId == stockId:
                position.updatePosition(transactionVolume)
                position.save()
                return
        # s = Stock(stockId=stockId)
        # s.save()
        p = Position(volume=transactionVolume, portfolio=self, stockId=stockId)
        p.save()
        # self.positions.append(Position(Stock(stockId), transactionVolume))

    def GetPortfolioValue(self):
        value = 0
        for position in self.positions:
            value += position.volume * float(getCurrentStockPrice(position.stockId)[1])
        return value

    def contains_stock(self, stockId: str) -> bool:
        for pos in self.positions:
            if pos.stockId == stockId:
                return True
        return False

    def get_volume_stock(self, stockId: str) -> float:
        for pos in self.positions:
            if pos.stockId == stockId:
                return float(pos.volume)
        return 0

    class Meta:
        database = db


class Position(Model):
    # def __init__(self, stock, volume):
    #     self.stock = stock
    #     self.volume = volume..
    volume = FloatField()
    portfolio = ForeignKeyField(Portfolio, backref='positions')
    stockId = CharField()
    # stock = ForeignKeyField(Stock, backref='positions')

    def updatePosition(self, volume):
        if self.volume + volume < 0:
            print('Negative position not allowed')
        else:
            self.volume += volume

    class Meta:
        database = db
