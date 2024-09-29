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

# * operator
a = [123, '*']
a *= 6
print(a)

# Quiz
# total = 0
# count = 0
# while(True):
#     prompt = input('Enter a number or (done to end): ')
#     if prompt == 'done': break
#     value = float(prompt)
#     total += value
#     count += 1
# average = total / count
    
# print(f'sum: {total} Average: {average}')

# Solution
mylist = [] #  I can also used: mylist = list()
while(True):
    prompt = input('Enter a number or (done t o end): ')
    if prompt == 'done': break
    value = float(prompt)
    mylist.append(value)
    mySum = sum(mylist)
    average = mySum / len(mylist)
    
print(f'sum: {mySum} Average: {average}')