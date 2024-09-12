#!/usr/bin/python3
# Calculates the highest common factor of a given number
def hcf(x, y):
    assert int(x) == x and int(y) == y, "The numbers must be integer only"
    if x < 0:
        x = -1 * x
    if y < 0:
        y = -1 * y
    if y == 0:
        return x
    else:
        return hcf(y, x%y)

print(hcf(-48, 1.8))