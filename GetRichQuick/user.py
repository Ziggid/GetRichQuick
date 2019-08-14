from peewee import *

from .Stock import getCurrentStockPrice

db = SqliteDatabase('getrich.db')


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

    @property
    def portfolio(self):
        return self._portfolio

    @property
    def transactions(self):
        return self._transactions

    def doTransaction(self, stockId: str, transactionVolume, orderType):
        response = getCurrentStockPrice(stockId)
        transaction_date = response[0]
        transaction_price = response[1]
        if orderType == 'buy':
            if self._balance > float(transaction_price) * float(transactionVolume):
                if transactionVolume > 0:
                    t = Transaction(_user=self, _stockId=stockId, _transactionDate=transaction_date,
                                    _transactionPrice=transaction_price, _transactionVolume=transactionVolume,
                                    _orderType=orderType)
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
            t = Transaction(_user=self, _stockId=stockId, _transactionDate=transaction_date,
                            _transactionPrice=transaction_price, _transactionVolume=transactionVolume,
                            _orderType=orderType)
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
            else:
                raise Exception("You don't have sufficient balance to complete the transaction. Transaction of " +
                                str(transaction.transactionVolume) + " " + str(transaction.stockId) +
                                " stock was denied. You needed " + str(transaction.transactionPrice) +
                                " Euro but only have a balance of " + str(self.balance))
        else:
            return False

    def EnoughVolumeForSellTransaction(self, transaction):
        if transaction.orderType == 'sell':
            if float(transaction.transactionVolume) < float(self.portfolio[0].get_volume_stock(transaction.stockId)):
                return True
            else:
                raise Exception("You don't have enough volume to carry out this transaction. Transaction of " + str(
                    transaction.transactionVolume) + ' ' + str(
                    transaction.stockId) + ' stocks was denied. You needed ' + str(
                    transaction.transactionVolume) + ', but only have a volume of ' + str(
                    self.portfolio[0].get_volume_stock(transaction.stockId)))
        else:
            print('this is a buy order type')

    class Meta:
        database = db


class Transaction(Model):
    _user = ForeignKeyField(User, backref='_transactions')
    _stockId = CharField()
    _transactionDate = CharField()
    _transactionPrice = FloatField()
    _transactionVolume = IntegerField()
    _orderType = CharField()

    @property
    def user(self):
        return self._user

    @property
    def stockId(self):
        return self._stockId

    @property
    def transactionDate(self):
        return self._transactionDate

    @property
    def transactionPrice(self):
        return self._transactionPrice

    @property
    def transactionVolume(self):
        return self._transactionVolume

    @property
    def orderType(self):
        return self._orderType

    def __str__(self):
        return 'A ' + str(self.orderType) + " of " + str(self.stockId) + " of size " + str(
            self.transactionVolume) + ' is executed on ' + str(self.transactionDate) + ' for the price of ' + str(
            self.transactionPrice)

    class Meta:
        database = db
