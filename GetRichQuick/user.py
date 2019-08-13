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
            self.balance -= float(transaction.transactionPrice) * float(transaction.transactionVolume)
            self.portfolio.AddPosition(transaction.stock.stockId, transaction.transactionVolume)
        elif transaction.orderType == 'sell':
            self.portfolio.AddPosition(transaction.stock.stockId, -transaction.transactionVolume)
            self.balance += float(transaction.transactionPrice) * float(transaction.transactionVolume)
        else:
            print("unknown order type: ", transaction.orderType)

    # Todo
    def getBalance(self):
        return self.balance

    def getPortfolioValue(self):
        return self.portfolio.GetPortfolioValue()
