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


