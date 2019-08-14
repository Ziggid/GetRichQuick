# from .Portfolio import Portfolio
import requests
from peewee import *
from .Stock import getCurrentStockPrice

db = SqliteDatabase('getrich.db')


# class Stock(Model):
#     # def __init__(self, stockId):
#     #     self.stockId = stockId
#     _stockId = CharField()
#
#     @property
#     def stockId(self):
#         return self._stockId
#
#     def getCurrentStockPrice(self):
#         response = requests.get(
#             "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + self.stockId +
#             "&interval=1min&outputsize=compact&apikey=HUTM7V18LBLQPIOP")
#
#         # Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
#         # See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
#         if response.status_code != 200:
#             raise ValueError("Could not retrieve data, code:", response.status_code)
#
#         # The service sends JSON data, we parse that into a Python datastructure
#         raw_data = response.json()
#         return [max(raw_data['Time Series (1min)'].keys()),
#                 raw_data['Time Series (1min)'][max(raw_data['Time Series (1min)'].keys())]['4. close']]
#
#     def __str__(self):
#         return 'The stock ' + str(self.stockId) + ' trades for ...' + ' on ' + str(self.date)
#
#     class Meta:
#         database = db


class User(Model):
    _name = CharField()
    _balance = FloatField()

    # This is interfering with peewee database. Staying with public variables for now.
    @property
    def name(self):
        return self._name

    @property
    def balance(self):
        return self._balance

    # transactions = [] # wordt backref
    # portfolio = ForeignKeyField(Portfolio, backref = "users") #logic is other way around

    # def __init__(self, name, startingbalance):
    #     self.name = name
    #     self.balance = startingbalance

    def doTransaction(self, stockId: str, transactionVolume, orderType):
        response = getCurrentStockPrice(stockId)
        transaction_date = response[0]
        transaction_price = response[1]
        if orderType == 'buy':
            if self._balance > float(transaction_price) * float(transactionVolume):
                if transactionVolume > 0:
                    t = Transaction(user=self, stockId=stockId, transactionDate=transaction_date,
                                    transactionPrice=transaction_price, transactionVolume=transactionVolume,
                                    orderType=orderType)
                    t.save()
                    self._balance -= float(transaction_price) * float(transactionVolume)
                    self.portfolio[0].addPosition(stockId, t.transactionVolume)
                else:
                    print("You cannot buy a negative amount")
            else:
                print("You don't have enough balance to carry out this transaction. Transaction of " + str(
                    transactionVolume) + ' ' + str(stockId) + ' stocks was denied. You needed ' + str(
                    float(transaction_price) * float(transactionVolume)) + ' euro, but only have a balance of '
                      + str(self._balance))
        elif orderType == 'sell':
            t = Transaction(user=self, stockId=stockId, transactionDate=transaction_date,
                            transactionPrice=transaction_price, transactionVolume=transactionVolume,
                            orderType=orderType)
            if (self.EnoughVolumeForSellTransaction(t)):
                t.save()
                self.portfolio[0].addPosition(stockId, -transactionVolume)
                self._balance += float(transaction_price) * float(transactionVolume)
        else:
            raise Exception("Unknown order type: " + str(orderType))
        self.save()

    def getPortfolioValue(self):
        return self.portfolio.GetPortfolioValue()

    def enough_balance_for_buy_transaction(self, transaction) -> bool:
        "checks if user has enough balance to do the buy transaction"
        if transaction.orderType == "buy":
            if self.balance > transaction.transactionPrice * transaction.transactionVolume:
                return True
            else: raise Exception("You don't have sufficient balance to complete the transaction. Transaction of " +
                                  str(transaction.transactionVolume) + " " + str(transaction.stockId) +
                                  " stock was denied. You needed " + str(transaction.transactionPrice) +
                                  " Euro but only have a balance of " +str(self.balance))
        else: return False

    def EnoughVolumeForSellTransaction(self, transaction):
        if transaction.orderType == 'sell':
            if float(transaction.transactionVolume) < float(self.portfolio[0].get_volume_stock(transaction.stockId)):
                return True
            else: raise Exception("You don't have enough volume to carry out this transaction. Transaction of " + str(
                    transaction.transactionVolume) + ' ' + str(
                    transaction.stockId) + ' stocks was denied. You needed ' + str(
                    transaction.transactionVolume) + ', but only have a volume of ' + str(
                        self.portfolio[0].get_volume_stock(transaction.stockId)))
        else: print('this is a buy order type')

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
    stockId = CharField()
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
