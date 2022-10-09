#9/27/2022
#Rachel Cewe
#CSD 205 - Module 9 - Banking Program


class BankAccount:
    """an attempt to model a bank account"""

    def __init__(self, accountNumber, balance):
        """Initialize attributes for BankAccount"""
        self.accountNumber = accountNumber
        self.balance = balance


    def withdrawl(self):
        """Subtract withdrawal amount from balance"""
        withdrawl = float(input("Please enter the amount you would like to withdraw: $"))
        self.balance -= withdrawl
        print(f"Your new balance is: $", self.balance)


    def deposit (self):
        """Add deposit to the balance"""
        deposit = float(input("Please enter the amount in which you would like to deposit: $"))
        self.balance += deposit
        print('Your new balance is: $', self.balance)


    def getBalance (self):
        """Display balance"""
        print(f"Your current balance is: $", self.balance)

        


class CheckingAccount (BankAccount):
    """Represents a Checking Account"""
    
    def __init__ (self, accountNumber, balance):
       """Initializes attributes from BankAccount"""
       super().__init__(accountNumber, balance)
       self.fees = float(5)
       self.minimumBalance = float(50)
       
    def checkMinimumBalance (self):
        """Check the minimum balance"""
        if self.balance < self.minimumBalance:
            print("Your account is below the minimum required balance to avoid fees")
        else: print (self.balance)
        
    def deductFees (self):
        """Deduct fee for not maintaining the minimum required balance"""
        if self.balance < self.minimumBalance:
            print('${} deduct fee has been incurred for not maintaining ${} minimum balance'.format(self.fees, self.minimumBalance))
        self.balance -= self.fees
        print ("Your new balance minus incurred fee is: $", self.balance)
        
        

class SavingsAccount (BankAccount):
    """Represents a Savings Account"""
    
    def __init__ (self, accountNumber, balance, interestRate):
       """Initializes attributes from BankAccount"""
       super().__init__(accountNumber, balance)
       self.interestRate = interestRate
       
    def addInterest (self):
        """Add interest to balance"""
        interest = self.balance * self.interestRate
        balancewithInterest = interest + self.balance
        print(f"Your new balance with interest added is ${balancewithInterest}.")

# The program        
def main():       
# Assigns title to variable ("title")
    title = "welcome to something of a bank"

# Prints the variable as a title
    print(title.title())
    print()

#Creates two objects with values
    my_check = CheckingAccount (8675309, 200)
    my_sav = SavingsAccount (90210, 200)

#Prints the current checking account balance
    print ("\nYour Checking Account Balance is: $", my_check.balance)
    print()
#Ask user if they would like to withdraw
    withdraw = input(("\nWould you like to withdraw from this account? (y/n):\t"))
    print()
    if withdraw == "y":
        my_check.withdrawl()
        my_check.deductFees()


    savingsBalance = input("\nWould you like to check your Savings Account Balance? (y/n):\t")
    print()
    if savingsBalance == "y":
        print ("\nYour Savings Account Balance is : $", my_sav.balance)
        my_sav.addInterest()

def another_transaction():
    while True:
        transaction = input("\n\t\tWould you like to do another transaction? 'Y' - 'N': ")
        transaction = transaction.title()
        if transaction == 'Y':
            main()
        else:
            break
    
main()
another_transaction()

print("\n\tThank you for banking with Python Bank.")
input("\n\t\tPress Enter to quit.")