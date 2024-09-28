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