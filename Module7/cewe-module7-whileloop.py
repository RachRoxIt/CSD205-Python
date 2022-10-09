#Rachel Cewe 9/9/22 Module7 - While loop


#Get the initial investment amount from the user
initialINVAMT = (float)(input("Enter your inital investment amount: "))
print()
#Get the annual interest rate from the user as a whole  number
interestRATE = (float)(input("Enter your annual interest rate: "))
print()
#Create the variables to be used in the while loop
totalAMOUNT = initialINVAMT
year = 0
double = initialINVAMT*2
#Loop should go until amount equals initial invest amount doubled
while totalAMOUNT <=double:
    year += 1
    totalAMOUNT += totalAMOUNT*interestRATE/100
    print(f"Year {year}\t{totalAMOUNT}") 
    print()
print(f"\nYour initial investment amount of $ {initialINVAMT} will double in {year} years!")