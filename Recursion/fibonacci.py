#!/usr/bin/python3

def fibonacci(n):
    result = []
    if n in [0, 1]:
        return n
    else:
        result.append(n)
        print(n, end=',')
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6))

