from array import *

arr1 = array('i', [1, 2, 3, 5, 3, 5])

# def accessElement(array, index):
#     if index >= len(array):
#         print("Index not in the array")
#     else:
#         print(array[index])

# accessElement(arr1, 5)

def searchArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The element does not exist in the array"

print(searchArray(arr1, 5))