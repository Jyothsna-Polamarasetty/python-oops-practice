
# Creating a class
class BankAccount:
    def __init__(self,account_number, account_name,balance):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance
    def Deposit(self, deposit_am):
        if deposit_am > 0:
            self.balance = self.balance + deposit_am
            print(f"Depositing {deposit_am} ot the account holder {self.account_name} with account number {self.account_number}")
        else:
            print("Invalid Amount")

    def Withdraw(self,withdraw_am):

        self.balance = self.balance - withdraw_am
        if self.balance >0:
            print("Deposit successful")
            print(f"Withdraw amount of {withdraw_am} to Account Number {self.account_number}")
        else:
            print("Balance cant be 0")

    def check_Balance(self):
        total_balance = self.balance
        print(f"Total Balance is {total_balance}")

ob1 = BankAccount(23456778,"Jyothsna",2000)
ob1.Deposit(2000)
ob1.Withdraw(4000)
ob1.check_Balance()


