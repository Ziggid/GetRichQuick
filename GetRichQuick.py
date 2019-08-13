from GetRichQuick.Stock import Stock
from GetRichQuick.Portfolio import Portfolio
from GetRichQuick.Portfolio import Position
from GetRichQuick.TransactionClass import Transaction
from GetRichQuick.user import User

from peewee import *

db = SqliteDatabase('getrich.db')

db.connect()
# db.create_tables([Portfolio, Position, Stock, Transaction, User])
for u in User.select():
    print(u.name)

# u = User(name="bart",balance=100000.00)
bart = User.select().where(User.name == "bart").get()

s = Stock(stockId="ING")
s.save()

t = Transaction(user=bart, stock=s, transactionDate=s.getCurrentStockPrice()[0],
                transactionPrice=s.getCurrentStockPrice()[1], transactionVolume=10, orderType='buy')
t.save()





# print("date =" + t.transactionDate)

# print(u.name, u.balance)
# u.save()
db.close()

# u = User("bart", 0)
# t = Transaction(10, "ING", "buy")
# t2 = Transaction(5, "ING", "sell")
#
# u.doTransaction(t)
# u.doTransaction(t2)
#
# for p in u.portfolio.positions:
#     print(str(p.stock.stockId) + ": " + str(p.volume))
#
# print(u.balance)
# print(u.getPortfolioValue())
