from flask import Flask, render_template, request, redirect
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
            result = User.select().where(User._name == name).get()
            print("Loading user: " + name)
            testbool = False
    if testbool:
        print("Creating new user " + name + ".")
        result = newUser(name, 100000.00)
    return result


db = SqliteDatabase('getrich.db')

db.connect()
# When you need to reset, uncomment the below code.
# db.drop_tables([Portfolio, Position, Transaction, User])
# db.create_tables([Portfolio, Position, Transaction, User])


# WebInterface
app = Flask(__name__)



@app.route('/main', methods=['GET', 'POST'])
def stock_form():
    username = ''
    if request.method == 'POST':
        username = request.form['user']
        global u
        u = loadUser(username)
        return redirect("http://127.0.0.1:5000/GetRichQuick", code=302)
    else:
        return render_template("User.html")

@app.route('/GetRichQuick', methods=['GET', 'POST'])
def interaction_client():
    if request.method == 'POST':
        stockId = request.form['stock']
        type = request.form['type']
        amount = request.form['amount']
        u.doTransaction(stockId, int(amount), type)
        u.save()

        return render_template("GetRichQuick.html",
                               name=u.name,
                               balance=u.balance)
    else:
        return render_template(
        "GetRichQuick.html",
        name=u.name,
        balance=u.balance
    )


@app.route('/')
def hello_world():
    return render_template("GetRichQuick.html")


if __name__ == '__main__':
    app.run(debug=True)

# loads user (or creates user if non-existing)
u = loadUser(input("Enter your name: "))
print("Current Cash-Balance is: " + str(u.balance))
print("printing current portfolio")
for pos in u.portfolio[0].positions:
    print(pos.stockId, pos.volume)

stockId = input("What stock? ")
ttype = input("buy/sell: ")
amount = int(input("how many? "))

u.doTransaction(stockId, amount, ttype)
u.save()
print("New Cash-Balance is: " + str(u.balance))
print("printing new portfolio")
for pos in u.portfolio[0].positions:
    print(pos.stockId, pos.volume)

db.close()
