#!/usr/bin/python3

def decimal2Binary(n):
    assert int(n) == n, "The parameter must be an integer only!"
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimal2Binary(int(n/2))