balance = 1000  # global account balance

def deposit(amount):
    global balance
    balance = balance + amount
    print("After deposit, balance =", balance)

def show_local_balance():
    balance = 0  # local to this function
    print("Inside local function, balance =", balance)

print("Start:", balance)
deposit(500)
print("Account balance:", balance)
show_local_balance()
print("Account balance still:", balance)
