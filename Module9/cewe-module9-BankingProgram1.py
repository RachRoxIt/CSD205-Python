#Rachel Cewe
#10/08/22
#Module 9 - Banking program REDO
#Here we go

minBalance = 50

class BankAccount:
    """an attempt to model a bank account"""

    def __init__(self, accountNumber, balance):
        """Initialize attributes for BankAccount"""
        self.accountNumber = accountNumber
        self.balance = balance


    def withdrawl(self):
        """Subtract withdrawal amount from balance"""
        withdrawl = float(input("Please enter the amount you would like to withdraw: $"))
        #self.balance = self.balance - withdrawl
        if withdrawl > self.balance:
            print("\nACCOUNT ALERT >>>>>>>>INSUFICIENT FUNDS<<<<<<<<")
            print()
        else:
            print(f"\n${withdrawl} has been withdrawn from account number {self.accountNumber}.")
            print()
        self.balance = self.balance - withdrawl       


    def deposit (self):
        """Add deposit to the balance"""
        deposit = float(input("Please enter the amount in which you would like to deposit: $ "))
        self.balance = self.balance + deposit
        print('Your new balance is: $', self.balance)
        if self.balance < minBalance:
            print("WARNING.  Your current balance remains less than the required minimum balance.  Please make a deposit to avoid incurring fees.")


    def getBalance (self):
        """Display balance"""
        print(f"Your current balance is: $", self.balance)



    
class CheckingAccount(BankAccount):

    """Represents a Checking Account"""

    def __init__(self, accountNumber, balance, fees, minimumBalance):
        super().__init__(accountNumber, balance)      #inherits variables and me
        self.fees = fees        #value passed into object for bank account fees, charged to account 
        self.minimumBalance = minimumBalance   #minimum balance amount determined by bank. used to d
        
    
    def deductFees (self):
        """Deduct fee for not maintaining the minimum required balance"""

        if self.balance < self.minimumBalance:
            self.balance = self.balance - self.fees
            print(f'A ${self.fees} deduct fee has been incurred for not maintaining the required $ {self.minimumBalance} minimum balance.')
            print ("Your new balance minus incurred fee is: $", self.balance)
            print("Please make a deposit to maintain your required minimum balance and avoid further deduct fees.")
            print()

    def checkMinimumBalance (self):
        """Check the minimum balance"""
        if self.balance < self.minimumBalance:
            print("Your account is below the minimum required balance to avoid fees")
            self.deductFees()
            print()


class SavingsAccount (BankAccount):
        
    """Represents a Savings Account"""  
    
    def __init__ (self, accountNumber, balance, interestRate = 0.02):
       """Initializes attributes from BankAccount"""
       super().__init__(accountNumber, balance)
       self.interestRate = interestRate
       
    def addInterest (self):
        """Add interest to balance"""
        interest = self.balance * self.interestRate
        balancewithInterest = interest + self.balance
        print(f"Your new balance with interest added is ${balancewithInterest}.")
       


#declare variables and assign values to them for using in a main menu:
accountOptions = {1: "Checking", 2: "Savings", 3: "Exit"}

checkMenu = {1: 'Deposit', 2: 'Withdraw', 3: 'Check Balance'}

saveMenu = {1: 'Deposit', 2: 'Withdraw', 3: 'Check Balance with interest'}

quitMenu = {1: 'Exit'}


# Now define a method that will display the main menu to the user. It should list all possible selections and ask user to make a selection from it.
def print_main_menu():
    print()
    print('Welcome to Something of a Bank!')
    print('\nAccount Options:')
    for keys in accountOptions.keys():
        print(keys, ':', accountOptions[keys])
    print()

def checkingMenu():
    print('\nChecking Options: ')
    for keys in checkMenu.keys():
        print(keys, ':', checkMenu[keys])
        print()

def savingsMenu():
    print('\nSavings Options: ')
    for keys in saveMenu.keys():
        print(keys, ':', saveMenu[keys])
        print()

def exitMenu():
    print('\n Enter 1 to exit:')
    for keys in quitMenu.keys():
        print(keys, ':', quitMenu[keys])
    

#Create a checking account and savings account object from their classes. Do this by assigning the class names to variable names.  Then pass the required arguments to each function by placing the values in the parenthesis.   
checkObject = CheckingAccount(123456, float(200), 5, 50)
saveObject = SavingsAccount(123457, 200, float(0.02) )

while (True):
    print_main_menu()

    while (True):  #here is where the menu will loop
        try:
            option = int(input("\nEnter Selection:\t"))
        except ValueError:
            print("\nInvalid Input. That is not a number.  Please enter a numerical value.")
            print()
            print_main_menu()
            continue
        else:
            break

    if option == 1:  #Options for choosing checking account
        checkingMenu()
        print(f"Current checking account balance is: $ {checkObject.balance}")
        print()
        option = int(input('What would you like to do with your Checking Account?:'))
        print()
        if option == 1:
            checkObject.deposit()
            print()
            print("***We will now return to the Main Menu where you may make another selection***")
            print()
        elif option == 2:
            checkObject.withdrawl()
            checkObject.checkMinimumBalance()
            print()
            print("***We will now return to the Main Menu where you may make another selection***")
            print()
        elif option == 3:
            checkObject.checkMinimumBalance()
            print()
            print("***We will now return to the Main Menu where you may make another selection***")
            print()
        

    elif option == 2:  #Options for choosing savings account
        savingsMenu()
        print(f"Current savings account balance is: $ {saveObject.balance}")
        option = int(input('What would  you like to do with your Savings Account?:'))
        print()
        if option == 1:
            saveObject.deposit()
            print()
            print("***We will now return to the Main Menu where you may make another selection***")
            print()
        elif option == 2:
            saveObject.withdrawl()
            print()
            print("***We will now return to the Main Menu where you may make another selection***")
            print()
        elif option == 3:
            saveObject.getBalance()
            saveObject.addInterest()
            print()
            print("***We will now return to the Main Menu where you may make another selection***")
            print()
        

    elif option == 3:  #Exits the program
        print("Thank you for banking with Something of a Bank.  Now go enjoy the silence")
        break

    else:
        break