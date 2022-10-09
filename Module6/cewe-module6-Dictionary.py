#Rachel Cewe 8/30/22 Module 6 Dictionary
#Create a dictionary including 10 key value pairs
dogs = {'boston': 'sociable', 'golden': 'loyal', 'bulldog': 'nonactive',  'labradoodle': 'hyperactive', 'germanshephard': 'protector', 'pointer': 'hunter', 'poodle': 'intelligent', 'pug': 'nonagressive', 'corgi': 'herder', 'shitzu': 'playful'}
print()
#Display all key values to user and ask them to select one
selection = dogs.keys()
print(selection)
user_selection = input("Please select your prefered breed:" )
#Then display the value paired to the key
print()
temperament = dogs.values()
print(temperament)