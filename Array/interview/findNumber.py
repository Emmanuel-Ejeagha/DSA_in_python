# This function finds a number in the array

import numpy as np

MyArray = np.array([1,2,3,4,5,6,7,8,9,0])

def findNum(array, target):
    for x in range(len(array)):
        if array[x] == target:
            print(f"{MyArray}\nNumber {target} is in index {x}")


findNum(MyArray, 6)