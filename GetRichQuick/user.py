class User:
    name = ""
    balance = 0
    transactions = []

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    #placeholder
    def transact(self):
        pass

u = User("bart", 100)

print(u.balance)