from peewee import *

from .Stock import getCurrentStockPrice
from .user import User

db = SqliteDatabase('getrich.db')


class Portfolio(Model):
    _user = ForeignKeyField(User, backref='_portfolio')

    @property
    def user(self):
        return (self._user)

    @property
    def positions(self):
        return (self._positions)

    def addPosition(self, stockId, transactionVolume):
        for position in self.positions:
            if position.stockId == stockId:
                position.updatePosition(transactionVolume)
                position.save()
                return
        p = Position(_volume=transactionVolume, _portfolio=self, _stockId=stockId)
        p.save()

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
    _volume = FloatField()
    _portfolio = ForeignKeyField(Portfolio, backref='_positions')
    _stockId = CharField()

    @property
    def volume(self):
        return (self._volume)

    @property
    def portfolio(self):
        return (self._portfolio)

    @property
    def stockId(self):
        return (self._stockId)

    def updatePosition(self, volume):
        if self._volume + volume < 0:
            print('Negative position not allowed')
        else:
            self._volume += volume

    class Meta:
        database = db
