# Searching for an element in a list
myList = [10, 20, 3, 5, 3,65,9]

def searchList(list, value):
    for num in list:
        if num == value:
            return list.index(value)
    return "The number is not in the list"

print(searchList(myList, 3))