#Use a function to convert miles to kilometers
#Incorporate try and except blocks
def convert_distance():
        kilometers = miles * 1.609
        print(f"At {miles} miles, your distance in kilometers converts to: {kilometers} km") 
#a While loop is used to run the program until the user enters a number (can potentially be a float)
miles = float
while miles == float:
    try: 
#Prompt the user for the number of miles driven
        miles = float(input("Enter number in miles driven: "))
        print()
    except ValueError:
        print()
        print("That is not a number. Please enter a number: ")
        print()
#Call a function that converts miles to kilometersS        
convert_distance()