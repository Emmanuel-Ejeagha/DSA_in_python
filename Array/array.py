from array import *

arr1 = array('i', [1, 2, 3, 5, 3, 5])

def accessElement(array, index):
    if index >= len(array):
        print("Index not in the array")
    else:
        print(array(arr1[index]))

accessElement(5)