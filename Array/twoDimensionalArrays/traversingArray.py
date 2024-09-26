import numpy as np

twoDArray = np.array([[2, 5, 65, 54],
                     [34, 2, 90, 4],
                     [30, 950, 24, 86],
                     [30, 16, 22, 9]])

print(twoDArray)

def traverseYDArray(array):
    for x in range(len(array)):
        for y in range(len(array[0])):
            print(array[x][y])


print(traverseYDArray(twoDArray))