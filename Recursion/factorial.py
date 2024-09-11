#!/usr/bin/python3
# factorial

def factorial(n):
    assert n>=0 and int(n) == n, "The number must be an integer"
    if n in [1, 0]:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))