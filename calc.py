
def calculate_sum(*args):
    tot = 0
    for number in args:
        tot += number

    return tot


def calculate_multiplication(*args):
    tot = 1
    for number in args:
        tot *= number

    return tot


def calculate_substraction(number1, number2):
    return number1 - number2


def calculate_division(numerator, denominator):
    return float(numerator)/ float(denominator)


=======
def add(*nums):
    return sum(nums)


def multiply(*nums):
    product = 1
    for num in nums:
        product *= num
    return product


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b if b != 0 else None

