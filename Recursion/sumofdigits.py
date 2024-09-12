#!/usr/bin/python3


def sumofdigits(num):
    assert num>=0 and int(num) == num, "The number has to be a postive integer only!"
    if num == 0:
        return 0
    else:
        return int(num % 10) + sumofdigits(int(num / 10))

print(sumofdigits(123451))

# def sumofdigits(num):
#     assert num >= 0 and isinstance(num, int), "The number has to be a positive integer only!"
#     if num == 0:
#         return 0
#     else:
#         return num % 10 + sumofdigits(num // 10)

# print(sumofdigits(123451))
