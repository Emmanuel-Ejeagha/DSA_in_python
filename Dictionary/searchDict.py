# Search for an element in a dictionary

myDict = {'name': 'Emmanuel', 'age': 20, 'state': 'Lagos', 'ethnicity': 'Igbo'}

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return f'The value {value} does not exist'

print(searchDict(myDict, 25))