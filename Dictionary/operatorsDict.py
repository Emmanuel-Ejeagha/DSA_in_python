# Operators and Built in functions

myDict = {'name': 'Emmanuel', 'age': 20, 'state': 'Lagos', 'ethnicity': 'Igbo'}

print('name' in myDict)

for key in myDict:
    print(key, myDict[key])


#  all()
newDict = {0: True, 1: False, 2: False}
print(all(newDict))
newDict = {1: True, 2: True}
print(all(newDict))
newDict = {}
print(all(newDict))
newDict = {0: False, 1: False, 2: False}
print(all(newDict))

# any() method
newDict = {0: True, 1: False, 2: False}
print(any(newDict))
newDict = {1: True, 2: True}
print(any(newDict))
newDict = {}
print(any(newDict))
newDict = {0: False, 1: False, 2: False}
print(any(newDict))

# sorted method
print(sorted(myDict))
print(sorted(myDict, reverse=True))
print(sorted(myDict, key=len))

