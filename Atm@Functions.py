def Show_menu():
    print("----- Atm -----\n 1. Balance \n 2. Deposit \n 3. Withdraw \n 4. Show Last 10 Transactions \n 5. Exit")
balance =int(input("Enter your initial balance: "))
transactions = []
def deposit(balance, amount):
    while amount <= 0:
        print("Deposit amount must be positive.")
        amount = int(input("Enter deposit amount: "))
    balance += amount
    transactions.append(f"Deposited: {amount}")
    return balance

def withdraw(balance, amount):
    if amount <= balance:
       balance -= amount
       transactions.append(f"Withdrew: {amount}")
    while amount < 0:
        print("Withdrawal amount must be positive")
        amount = int(input("Enter withdrawal amount: "))
    while amount > balance:
        print("Insufficient funds.")
        amount = int(input("Enter a valid withdrawal amount: "))
    balance -= amount
    return balance
def get_last_transactions(transactions):
    return transactions[-10:]
def exit_program():
    print("Exiting the program. Thank you for Using our services!")
Show_menu()
Choice = int(input("Enter your choice: "))
if Choice == 1:
    print("Current Balance:", balance)
    transactions.append(f"Checked Balance: {balance}")
elif Choice == 2:
    amount = int(input("Enter deposit amount: "))
    balance = deposit(balance, amount)
elif Choice == 3:
    amount = int(input("Enter withdrawal amount: "))
    balance = withdraw(balance, amount)
elif Choice == 4:
    last_transactions = get_last_transactions(transactions)
    print("Last 10 Transactions:")
    for transaction in last_transactions:
        print(transaction)
elif Choice == 5:
    exit_program()