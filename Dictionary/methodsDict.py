# Dictionary Methods

myDict = {'name': 'Emmanuel', 'age': 20, 'state': 'Lagos', 'ethnicity': 'Igbo'}
# clear dictionary
myDict.clear()
print(myDict)

# copy dictionary
myDict = {'name': 'Emmanuel', 'age': 20, 'state': 'Lagos', 'ethnicity': 'Igbo'}
newDict = myDict.copy()
print(newDict)

# fromkeys method
newDict = myDict.fromkeys([1,2,3,4], 'Alpha')
print(newDict)

#  get() method
print(myDict.get('status'))
print(myDict)

# items() method
print(myDict.items())

# keys() method
print(myDict.keys())

# popitem() method
print(myDict.popitem())
print(myDict)

# setdefault() method
print(myDict.setdefault('status', 'single'))
print(myDict)

# values() method
print(myDict.values())

# update() method
myDict = {'name': 'Emmanuel', 'age': 20, 'state': 'Lagos', 'ethnicity': 'Igbo'}
newDict = {'occupation': 'Software Engineer', 'Education': "Degree"}
myDict.update(newDict)
print(myDict)