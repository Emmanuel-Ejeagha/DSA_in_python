# This Function Rotates Matrix Image [Leetcode]

import numpy as np

myArray = np.array([[1,2,3], [4,5,6], [7,8,9]])

def rotateMatrixImage(matrix):
    x = len(matrix)
    for layer in range(x//2):
        first = layer
        last = x - layer - 1
        for i in range(first, last):
            # save top element
            top = matrix[layer][i]
            # move left elements to top
            matrix[layer][i] = matrix[-i-1][layer]
            # move botttom element to left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            # move right to bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            # move to top right
            matrix[i][-layer-1] = top
    return matrix

print(myArray)
print(rotateMatrixImage(myArray))