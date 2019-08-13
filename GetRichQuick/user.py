# from .Portfolio import Portfolio
from peewee import *
import requests

db = SqliteDatabase('getrich.db')


class Stock(Model):
    # def __init__(self, stockId):
    #     self.stockId = stockId
    stockId = CharField()

    def getCurrentStockPrice(self):
        response = requests.get(
            "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + self.stockId +
            "&interval=1min&outputsize=compact&apikey=HUTM7V18LBLQPIOP")

        # Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
        # See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
        if response.status_code != 200:
            raise ValueError("Could not retrieve data, code:", response.status_code)

        # The service sends JSON data, we parse that into a Python datastructure
        raw_data = response.json()
        return [max(raw_data['Time Series (1min)'].keys()),
                raw_data['Time Series (1min)'][max(raw_data['Time Series (1min)'].keys())]['4. close']]

    def __str__(self):
        return 'The stock ' + str(self.stockId) + ' trades for ...' + ' on ' + str(self.date)

    class Meta:
        database = db


class User(Model):
    name = CharField()
    balance = FloatField()

    # transactions = [] # wordt backref
    # portfolio = ForeignKeyField(Portfolio, backref = "users") #logic is other way around

    # def __init__(self, name, startingbalance):
    #     self.name = name
    #     self.balance = startingbalance

    def doTransaction(self, stock, transactionVolume, orderType):
        transactionDate = stock.getCurrentStockPrice()[0]
        transactionPrice = stock.getCurrentStockPrice()[1]
        if orderType == 'buy':
            if self.balance > float(transactionPrice) * float(transactionVolume):
                if transactionVolume > 0:
                    t = Transaction(user=self, stock=stock, transactionDate=transactionDate,
                                    transactionPrice=transactionPrice, transactionVolume=transactionVolume,
                                    orderType=orderType)
                    t.save()
                    self.balance -= float(transactionPrice) * float(transactionVolume)
                    self.portfolio[0].addPosition(stock.stockId, t.transactionVolume)
                else:
                    print("You cannot buy a negative amount")
            else:
                print("You don't have enough balance to carry out this transaction")
        elif orderType == 'sell':
            t = Transaction(user=self, stock=stock, transactionDate=transactionDate,
                            transactionPrice=transactionPrice, transactionVolume=transactionVolume,
                            orderType=orderType)
            t.save()
            self.portfolio[0].addPosition(stock.stockId, -transactionVolume)
            self.balance += float(transactionPrice) * float(transactionVolume)
        else:
            print("unknown order type: ", transaction.orderType)

            self.save()

    def getPortfolioValue(self):
        return self.portfolio.GetPortfolioValue()

    class Meta:
        database = db


class Transaction(Model):
    # def __init__(self, transactionVolume, stockId, orderType):
    #     self.stock = Stock(stockId)
    #     pricetuple = self.stock.getCurrentStockPrice()
    #     self.transactionDate = pricetuple[0]
    #     self.transactionPrice = pricetuple[1]
    #     self.transactionVolume = transactionVolume
    #     self.orderType = orderType
    user = ForeignKeyField(User, backref='transactions')
    stock = ForeignKeyField(Stock, backref="transactions")
    transactionDate = CharField()
    transactionPrice = FloatField()
    transactionVolume = IntegerField()
    orderType = CharField()

    def __str__(self):
        return 'A ' + str(self.orderType) + " of " + str(self.stock.stockId) + " of size " + str(
            self.transactionVolume) + ' is executed on ' + str(self.transactionDate) + ' for the price of ' + str(
            self.transactionPrice)

    class Meta:
        database = db
