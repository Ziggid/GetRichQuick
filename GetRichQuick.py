from GetRichQuick.TransactionClass import Transaction
from GetRichQuick.user import User
#from GetRichQuick.Stock import Stock


u = User("bart", 10000)
t = Transaction(1, 100, 10, "google", "buy")
t2 = Transaction(1, 55, 10, "google", "sell")

u.doTransaction(t)
u.doTransaction(t2)

for p in u.getPortfolio():
    print(str(p) + ": " + str(u.getPortfolio()[p]))



print(u.balance)