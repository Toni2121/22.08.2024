import math


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def power(num1 :int, power1):
    power2 = num1 ** power1
    return power2

def sqrt(num1):
    sqrt1 = math.sqrt(num1)
    return sqrt1

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def factorial(num):
    if num == 0 or num == 1:
        return 1

    if num < 0:
        raise ValueError("factorial not defined for negative values")
    factorial1 = 1
    for i in range(1, num + 1):
        factorial1 = factorial1 * i

    return factorial1
# testing:
# check all cases
# auto keep functionality working
# make QA life more simple
# keep bug fix working