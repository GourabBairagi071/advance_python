# 3.Banking System with Transactions 
# Simulate real-time transactions between bank accounts. 
# Handle errors like overdraft, transaction timeout, incorrect account numbers.


import random
import threading
import time


class InsufficientBalance(Exception):
    pass


class InvalidAccount(Exception):
    pass


class TransactionTimeout(Exception):
    pass


class TransactionLimitExceeded(Exception):
    pass


class Bank:

    def __init__(self):
        self.accounts = {}
        self.transactions = []
        self.suspicious_transactions = []
        self.lock = threading.Lock()
        self.daily_limit = 50000

    def generate_account_number(self):

        while True:
            acc_no = random.randint(1000000000, 1009999999)

            if acc_no not in self.accounts:
                return acc_no

    def create_account(self, name, balance):

        acc_no = self.generate_account_number()

        self.accounts[acc_no] = {
            "name": name,
            "balance": balance
        }

        print("Account created successfully")
        print("Your Account Number:", acc_no)

    def deposit(self, acc_no, amount):

        if acc_no not in self.accounts:
            raise InvalidAccount("Account not found")

        self.accounts[acc_no]["balance"] += amount

        self.transactions.append(
            f"Deposit {amount} -> {acc_no}"
        )

        print("Deposit successful")

    def withdraw(self, acc_no, amount):

        if acc_no not in self.accounts:
            raise InvalidAccount("Account not found")

        if self.accounts[acc_no]["balance"] < amount:
            raise InsufficientBalance("Insufficient balance")

        self.accounts[acc_no]["balance"] -= amount

        self.transactions.append(
            f"Withdraw {amount} <- {acc_no}"
        )

        print("Withdrawal successful")

    def transfer(self, sender, receiver, amount):

        with self.lock:

            if sender not in self.accounts or receiver not in self.accounts:
                raise InvalidAccount("Invalid account number")

            if amount > self.daily_limit:

                msg = f"Suspicious Transaction: {sender} tried to send {amount}"

                self.suspicious_transactions.append(msg)

                raise TransactionLimitExceeded(
                    "Transaction limit exceeded (Max 50000)"
                )

            if self.accounts[sender]["balance"] < amount:
                raise InsufficientBalance("Insufficient balance")

            delay = random.randint(1,4)
            time.sleep(delay)

            if delay > 3:
                raise TransactionTimeout("Transaction timeout")

            self.accounts[sender]["balance"] -= amount
            self.accounts[receiver]["balance"] += amount

            self.transactions.append(
                f"{sender} -> {receiver} : {amount}"
            )

            print("Transfer successful")

    def check_balance(self, acc_no):

        if acc_no not in self.accounts:
            raise InvalidAccount("Account not found")

        print("Balance:", self.accounts[acc_no]["balance"])

    def show_transactions(self):

        print("\nTransaction History")

        if len(self.transactions) == 0:
            print("No transactions yet")
            return

        for t in self.transactions:
            print(t)

    def show_suspicious_transactions(self):

        print("\nSuspicious Transactions")

        if len(self.suspicious_transactions) == 0:
            print("No suspicious activity")
            return

        for s in self.suspicious_transactions:
            print(s)

    def show_accounts(self):

        print("\nAll Accounts")

        if len(self.accounts) == 0:
            print("No accounts created")
            return

        for acc in self.accounts:
            print(
                acc,
                self.accounts[acc]["name"],
                self.accounts[acc]["balance"]
            )


bank = Bank()



def menu():

    while True:

        print("\n------ Banking System ------")
        print("1 Create Account")
        print("2 Deposit")
        print("3 Withdraw")
        print("4 Transfer")
        print("5 Check Balance")
        print("6 Transaction History")
        print("7 Show All Accounts")
        print("8 Suspicious Transactions")
        print("9 Exit")

        choice = input("Enter choice: ")

        try:

            if choice == "1":

                name = input("Enter Name: ")
                balance = float(input("Initial Balance: "))

                bank.create_account(name, balance)

            elif choice == "2":

                acc = int(input("Account Number: "))
                amt = float(input("Amount: "))

                bank.deposit(acc, amt)

            elif choice == "3":

                acc = int(input("Account Number: "))
                amt = float(input("Amount: "))

                bank.withdraw(acc, amt)

            elif choice == "4":

                sender = int(input("Sender Account: "))
                receiver = int(input("Receiver Account: "))
                amt = float(input("Amount: "))

                bank.transfer(sender, receiver, amt)

            elif choice == "5":

                acc = int(input("Account Number: "))
                bank.check_balance(acc)

            elif choice == "6":

                bank.show_transactions()

            elif choice == "7":

                bank.show_accounts()

            elif choice == "8":

                bank.show_suspicious_transactions()

            elif choice == "9":

                print("Thank you")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)


menu()