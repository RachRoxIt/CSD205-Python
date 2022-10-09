# 9/27/22
# Rachel Cewe
# CSD 205 Module 9
# File processing 

import os

# prompt the user for directory
directory = input("Enter directory to save file: ")

# the directory defaults to current directory if user presses enter key
if directory == "":
  directory = "."

# prompt user for filename
filename = input("Enter filename: ")

# prompt for user details
name = input("Enter name: ")
address = input("Enter address: ")
phone = input("Enter phone number: ")

# create file object to write to specified file in directory
with open("{}/{}.csv".format(directory, filename), 'w') as file_object:
  file_object.write(",".join([name, address, phone]))

# create file object to read from specified file in directory
with open("{}/{}.csv".format(directory, filename), 'r') as file_object:
  print("{}/{}.csv contents".format(directory, filename))

  # loop through each line in file and print to screen
  for line in file_object:
    print(line)