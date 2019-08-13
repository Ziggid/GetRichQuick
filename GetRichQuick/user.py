from .Portfolio import Portfolio

class User:
    name = ""
    balance = 0
    transactions = []
    portfolio = Portfolio()

    def __init__(self, name, startingbalance):
        self.name = name
        self.balance = startingbalance


    def doTransaction(self, transaction):
        self.transactions.append(transaction)
        if transaction.orderType == 'buy':
            if self.balance > float(transaction.transactionPrice) * float(transaction.transactionVolume):
                if transaction.transactionVolume > 0:
                    self.balance -= float(transaction.transactionPrice) * float(transaction.transactionVolume)
                    if transaction.stock.stockId not in self.portfolio.keys():
                        self.portfolio[transaction.stock.stockId] = 0
                        self.portfolio[transaction.stock.stockId] += transaction.transactionVolume
                        self.balance -= float(transaction.transactionPrice) * float(transaction.transactionVolume)
                        self.portfolio.AddPosition(transaction.stock.stockId, transaction.transactionVolume)
                else:
                    print("You cannot buy a negative amount")
            else:
                print("You don't have enough balance to carry out this transaction")
        elif transaction.orderType == 'sell':
            self.portfolio.AddPosition(transaction.stock.stockId, -transaction.transactionVolume)
            self.balance += float(transaction.transactionPrice) * float(transaction.transactionVolume)
        else:
            print("unknown order type: ", transaction.orderType)


    # Todo

    def getPortfolioValue(self):
        return self.portfolio.GetPortfolioValue()
