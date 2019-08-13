from GetRichQuick.Stock import Stock
from GetRichQuick.TransactionClass import Transaction
from GetRichQuick.user import User


u = User("bart", 0)
t = Transaction(10, "ING", "buy")
t2 = Transaction(5, "ING", "sell")

u.doTransaction(t)
u.doTransaction(t2)

for p in u.portfolio.positions:
    print(str(p.stock.stockId) + ": " + str(p.volume))

print(u.balance)
print(u.getPortfolioValue())