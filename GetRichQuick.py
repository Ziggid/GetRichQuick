from GetRichQuick.Portfolio import Portfolio
from GetRichQuick.Portfolio import Position
from GetRichQuick.user import Transaction
from GetRichQuick.user import User
from peewee import *


def newUser(name, amount):
    temp = User(_name=name, _balance=amount)
    temp.save()
    portf = Portfolio(_user=temp)
    portf.save()
    return temp


def loadUser(name):
    testbool = True

    for user in User.select():
        if user.name == name:
            result = User.select().where(User.name == name).get()
            print("Loading user: " + name)
            testbool = False
    if testbool:
        print("Creating new user " + name + ".")
        result = newUser(name, 100000.00)
    return result

db = SqliteDatabase('getrich.db')

db.connect()
# When you need to reset, uncomment the below code.
db.drop_tables([Portfolio, Position, Transaction, User])
db.create_tables([Portfolio, Position, Transaction, User])

# loads user (or creates user if non-existing
u = loadUser(input("Enter your name: "))
print("Current Cash-Balance is: " + str(u.balance))
print("printing current portfolio")
for pos in u.portfolio[0].positions:
    print(pos.stockId, pos.volume)


stockId=input("What stock? ")
ttype = input("buy/sell: ")
amount = int(input("how many? "))

u.doTransaction(stockId, amount, ttype)
u.save()
print("New Cash-Balance is: " + str(u.balance))
print("printing new portfolio")
for pos in u.portfolio[0].positions:
    print(pos.stockId, pos.volume)

# bart = User.select().where(User.name == "bart").get()
# print(len(u.portfolio))
# for pos in bart.portfolio[0].positions
#     print(pos.stock.stockId, pos.volume)

#
# portf = Portfolio(user=bart)
# portf.save()

# bart = User.select().where(User.name == "bart").get()

# print("date =" + t.transactionDate)

# print(u.name, u.balance)
# u.save()
db.close()






