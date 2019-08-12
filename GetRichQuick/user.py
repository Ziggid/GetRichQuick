class User:
    name = ""
    balance = 0
    transactions = []
    portfolio = dict()

    def __init__(self, name, startingbalance):
        self.name = name
        self.balance = startingbalance


    def doTransaction(self, transaction):
        self.transactions.append(transaction)
        if transaction.orderType == 'buy':
            self.balance -= transaction.transactionPrice * transaction.transactionVolume
            if transaction.stockId not in self.portfolio.keys():
                self.portfolio[transaction.stockId] = 0
            self.portfolio[transaction.stockId] += transaction.transactionVolume
        elif transaction.orderType == 'sell':
            if transaction.stockId not in self.portfolio.keys():
                print(transaction.stockId + " not in portfolio!")
            self.portfolio[transaction.stockId] -= transaction.transactionVolume
            self.balance += transaction.transactionPrice * transaction.transactionVolume
        else:
            print("unknown order type: ", transaction.orderType)

    # Todo
    def getBalance(self):
        return self.balance



    # Todo
    def getPortfolio(self):
        return self.portfolio