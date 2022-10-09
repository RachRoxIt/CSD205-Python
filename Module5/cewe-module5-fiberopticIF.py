# Rachel Cewe 8/27/22 Cable IF/Mod 5
# To calculate cost of cable install
# Display welcome message for the program
print("Welcome to the fiber optic installation calculator")
print()
# Prompt user for company name
companyName = input("Enter company name: ")
print()
# Prompt user for number of feet to be installed
totalFeet = int(input("Enter total number of feet you'd like to have installed: ")) 
# Cost per square foot of cable is .87
print()
cost_perSqft = (.87)
discount_01 = (.80)
discount_02 = (.70)
discount_03 = (.50)
if totalFeet < 100:
    totalCost = (totalFeet*cost_perSqft)
elif totalFeet < 250:
    totalCost = (totalFeet*discount_01)
elif totalFeet <500:
    totalCost = (totalFeet*discount_02)
else:
    totalCost = (totalFeet*discount_03)
print()
print(f"Total estimate for {companyName} at {totalFeet} square feet is ${totalCost}.")

