lists = [1, 'man', 'woman', 23, 50, 'king']
print(lists)

b = 1 in lists
print(b)
print('bread' in lists)
print(lists[2])

# Tranversing through a list
for li in lists:
    print(li)

for i in range(len(lists)):
    lists[i] = str(lists[i])+ "+"
    print(lists[i])

# Tranversing through an empty list will not work
empty = []
for i in empty:
    print("I am empty")

# List operations / functions
a = [123, '*']
a *= 6
print(a)