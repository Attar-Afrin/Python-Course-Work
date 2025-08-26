from abc import ABC,abstractmethod
class BankAccount:
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    def checkbalance(self):
        pass
    @abstractmethod
    def history(self):
        pass



class CurrentAccount(BankAccount):
    def deposit(self):
        print("Unlimited Deposit At any Time ")
    def withdraw(self):
        print("Unlimited Withdraw At Any Time")
    def checkbalance(self):
        print("You can check your Balance")
    def history(self):
        print("You can see the history")


class SavingAccount(BankAccount):
    def deposit(self):
        print("Unlimited Deposit At any Time ")
    def withdraw(self):
        print("Unlimited Withdraw At Any Time")
    def checkbalance(self):
        print("You can check your Balance")
    def history(self):
        print("You can see the history")




class FixedDeposit(BankAccount):
    def deposit(self):
        print("Deposit At one Time ")
    def withdraw(self):
        print("Withdraw After period of Time")
    
Afreen=CurrentAccount()
Afreen.withdraw()
Afreen.history()
Afreen.deposit()
Afreen.checkbalance()

Harini=FixedDeposit()
Harini.withdraw()

Harini.history()
Harini.deposit()
Harini.checkbalance()



