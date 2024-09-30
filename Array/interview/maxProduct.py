# Maxmium Product

import numpy as np

myArray = np.array([1,32,3,13,5,31,6,9,54])

def findMaxProduct(array):
    maxProduct = 0
    for x in range(len(array)):
        for y in range(x+1, len(array)):
            if array[x] * array[y] > maxProduct:
                maxProduct = array[x] * array[y]
                pairs = str(array[x]) +" and "+ str(array[y])
    print(f"The Maximuim product in \n {myArray} is {pairs} \n = {maxProduct}")
    
findMaxProduct(myArray)