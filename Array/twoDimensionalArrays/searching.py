import numpy as np

twoDArray = np.array([[2, 5, 65, 54],
                     [34, 2, 90, 4],
                     [30, 950, 24, 86],
                     [30, 6, 4, 9]])

print(twoDArray)

def search2DArray(array, value):
    for x in range(len(array)):
        for y in range(len(array[0])):
            if array[x][y] == value:
                return 'The value is located at index '+ str(x)+" "+ str(y)
    return 'The element is not found'

print(search2DArray(twoDArray, 2))