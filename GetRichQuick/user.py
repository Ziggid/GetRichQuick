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
            if self.balance >0:
                self.balance -= float(transaction.transactionPrice) * float(transaction.transactionVolume)
                if transaction.stock.stockId not in self.portfolio.keys():
                    self.portfolio[transaction.stock.stockId] = 0
                    self.portfolio[transaction.stock.stockId] += transaction.transactionVolume
            else:
                print("You don't have enough balance to carry out this transaction")
        elif transaction.orderType == 'sell':
            if transaction.stock.stockId not in self.portfolio.keys():
                print(transaction.stock.stockId + " not in portfolio!")
            self.portfolio[transaction.stock.stockId] -= transaction.transactionVolume
            self.balance += float(transaction.transactionPrice) * float(transaction.transactionVolume)
        else:
            print("unknown order type: ", transaction.orderType)


    # Todo

#    def getBalance(self):
#        return self.balance



   # Todo
 #  def getPortfolio(self):
 #      return self.portfolio

