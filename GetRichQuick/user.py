from TransactionClass import Transaction

class User:
    name = ""
    balance = 0
    transactions = []
    portfolio = dict()

    def __init__(self, name, startingbalance):
        self.name = name
        self.balance = startingbalance


    def doTransaction(self, transaction):
        self.transactions.add(transaction)
        if transaction.orderType == 'buy':
            self.balance -= transaction.transactionPrice * transaction.transactionVolume
            if transaction.stockId not in portfolio.keys():
                portfolio[transaction.stockId] = 0
            portfolio[transaction.stockId] += transaction.transactionVolume
        elif transaction.orderType == 'sell':
            if transaction.stockId not in portfolio.keys():
                print(transaction.stockId + " not in portfolio!")
            portfolio[transaction.stockId] += transaction.transactionVolume
            self.balance += transaction.transactionPrice * transaction.transactionVolume
        else:
            print("unknown order type: ", transaction.orderType)

    # Todo
    def getBalance(self):
        return self.balance



    # Todo
    def getPortfolio(self):
        pass


u = User("bart", 100)
t = Transaction(1, 100, 20, "google", "buy")


print(u.balance)