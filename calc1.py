def summing_numbers(*args):
    answer = 0
    for number in args:
        number_int = int(number)
        answer += number_int
    return answer


def multiplying_numbers(*args):
    start_number = 0
    for number in args:
        number_int = int(number)
        answer = start_number * number_int
        start_number = number_int
    return answer


def subtracting_numbers(number1, number2):

    answer = int(number1) - int(number2)
    return answer


def dividing_numbers(number1, number2):
    answer = int(number1) / float(number2)
    return answer

