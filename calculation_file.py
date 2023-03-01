from calc import *

done = False

calc_type = input("What type of calculation do you want to perform (+, -, x, /)?")

while not done:
    input_numbers = input("what are your input values? (seperated by a space)")
    input_numbers = input_numbers.strip().split(" ")

    if calc_type == '+' or calc_type == 'x':
        try:
            len(input_numbers) >= 2
        except ValueError as e:
            print("input must be at least 2 numbers")

        try:
            answer = summing_numbers(*input_numbers)
            print(answer)
        except ValueError as e:
            print("Input must be numbers")

    elif calc_type == '-' or calc_type == '/':
        try:
            if len(input_numbers) != 2:
                raise ValueError
        except ValueError as e:
            print("Input must be 2 numbers")

        try:
            answer = subtracting_numbers(*input_numbers)
            print(answer)
        except ValueError as e:
            print("Input must be numbers")

    if calc_type == 'done':
        done = True
    else:
        calc_type = input("What is your next calculation (+, -, x, /)?")
