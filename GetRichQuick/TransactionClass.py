# from .Stock import Stock
# # from .user import User
# from peewee import *
#
# db = SqliteDatabase('getrich.db')
#
# class Transaction(Model):
#     # def __init__(self, transactionVolume, stockId, orderType):
#     #     self.stock = Stock(stockId)
#     #     pricetuple = self.stock.getCurrentStockPrice()
#     #     self.transactionDate = pricetuple[0]
#     #     self.transactionPrice = pricetuple[1]
#     #     self.transacti)onVolume = transactionVolume
#     #     self.orderType = orderType
#     user = ForeignKeyField(User, backref='transactions')
#     stock = ForeignKeyField(Stock, backref="transactions")
#     transactionDate = CharField()
#     transactionPrice = FloatField()
#     transactionVolume = IntegerField()
#     orderType = CharField()
#
#     def __str__(self):
#        return 'A ' + str(self.orderType) + " of " + str(self.stock.stockId) + " of size " + str(self.transactionVolume) + ' is executed on ' + str(self.transactionDate) + ' for the price of ' + str(self.transactionPrice)
#
#     class Meta:
#         database = db
