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
