# Tranversing through a dictionary

myDict = {'name': 'Emmanuel', 'age': 20, 'state': 'Lagos', 'ethnicity': 'Igbo'}

def traverseDict(my_dict):
    for key in my_dict:
        print(str(key) +": "+ str(my_dict[key]))

traverseDict(myDict)

