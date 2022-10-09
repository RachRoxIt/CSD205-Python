# Rachel Cewe 8/18/22 Cable installation cost/Mod 3
# To calculate cost of cable install
# Display welcome message for the program
print("Welcome to the fiber optic installation calculator")
# Prompt user for company name
companyName = input("Enter company name: ")
# Prompt user for number of feet to be installed
totalFeet = int(input("Enter total number of feet you'd like to have installed: "))
# Cost per square foot of cable is .87
n = (.87)
print("Total estimate for ", companyName, "is ", totalFeet*n)