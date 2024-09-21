# Two dimensional arrays pactical
import numpy as np

twoDArray = np.array([[2, 5, 65, 54],
                     [34, 2, 90, 4],
                     [30, 950, 24, 86],
                     [30, 16, 22, 9]])

print(type(twoDArray), twoDArray)

# Inserting a new column into the array
new2DArray = np.insert(twoDArray, 0, [[200, 9, 3, 8]], axis=1)
print(new2DArray)

# Inserting a new row into the array
new2DArray = np.insert(twoDArray, 0, [[11, 200, 9, 3]], axis=0)
print(new2DArray)