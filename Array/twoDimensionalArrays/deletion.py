import numpy as np

twoDArray = np.array([[2, 5, 65, 54],
                     [34, 2, 90, 4],
                     [30, 950, 24, 86],
                     [30, 16, 22, 9]])

print(twoDArray)

new2DArray = np.delete(twoDArray, 1, axis=1)
print(new2DArray)