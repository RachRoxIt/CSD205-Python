# Initialize a tuple with 15 to 25 related values
famNames = ( "Blanche", "Robert", "Paul", "Anthony", "Joseph", "Andy", "Solinda", "Angelica", "Celeste", "Elena", "Amber" , "Adam", "Rachel" , "Olivia", "Gloria")
# Display the contents in a single statement.
print(famNames)
# Iterate through the collection displaying the output as a single complete sentence for each value. Use the f-string format to control the output.
print()
# using a for loop to iterate through the collection.
for x in famNames:
    print(x)
mom = "Blanche"
dad = "Robert"
brother_1 = "Paul"
brother_2 = "Anthony"
brother_3 = "Joseph"
sis_inlaw_1 = "Andy" 
sis_inlaw_2 = "Solinda"
niece_1 = "Angelica"
niece_2 = "Celeste"
niece_3 = "Elena"
niece_4 = "Amber"
husband = "Adam"
wife = "Rachel"
daughter = "Olivia"
stepmom = "Gloria"
print()
#Using an f string to control the output
allFAM = f'{mom} {dad} {brother_1} {brother_2} {brother_3} {sis_inlaw_1} {sis_inlaw_2} {niece_1} {niece_2} {niece_3} {niece_4} {husband} {wife} {daughter} {stepmom}'
print(f'{mom}\n{dad}\n{brother_1}\n{brother_2}\n{brother_3}\n{sis_inlaw_1}\n{sis_inlaw_2}\n{niece_1}\n{niece_2}\n{niece_3}\n{niece_4}\n{husband}\n{wife}\n{daughter}\n{stepmom}')