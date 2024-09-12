#!/usr/bin/python3

def power(base, expo):
    assert expo >= 0 and int(expo) == expo, "The exponent most be intergers only"
    if expo == 0:
        return 1
    if expo == 1:
        return base
    return base * power(base, expo - 1)

print(power(2, 1.6))