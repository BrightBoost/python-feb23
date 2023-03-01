import calc

print("For addition: +")
print("For substraction: -")
print("For multiplication: x")
print("For division: /")

calculation_functions = {"+": calc.calculate_sum,
                         "-": calc.calculate_substraction,
                         "x": calc.calculate_multiplication,
                         "/": calc.calculate_division}

def write_good_calc():
    f = open("good_calcs.txt","a")
    f.write("Calculation succesfull")
    f.write('\n')
    f.close()

def write_error(error):
    f = open("bad_calcs.txt", "a")
    f.write("Calculation failed")
    f.write('\n')
    f.write(str(error))
    f.write('\n\n')

    f.close()

def ask_calc_type():
    done_calc_type = False
    while not done_calc_type:
        try:
            type_calculation = input("What calculation do you want to perform?")
            if type_calculation not in calculation_functions.keys():
                raise ValueError("Type of calculation filled in is not correct")
            else:
                done_calc_type = True
            function = calculation_functions[type_calculation]
            return type_calculation, function

        except ValueError as e:
            print(e)




def ask_numbers(type_calculation):
    done_ask_numbers = False
    while not done_ask_numbers:
        try:
            if type_calculation in ["+", "x"]:
                input_numbers = input(
                    "Please enter multiple numbers separated by a space")
                input_numbers = input_numbers.strip().split(" ")
                if len(input_numbers) < 1:
                    raise ValueError("No numbers filled in")

            elif type_calculation in ["-", "/"]:
                input_numbers = input("Please enter 2 numbers separated by a space")
                input_numbers = input_numbers.strip().split(" ")
                if len(input_numbers) != 2:
                    raise ValueError("More or less than two numbers are filled in")

            input_numbers = [float(x) for x in input_numbers]
            done_ask_numbers = True
            return input_numbers

        except ValueError as e:
            print(e)
            write_error(e)

done_total = False
while not done_total:

    calc_type, function = ask_calc_type()
    input_numbers = ask_numbers(calc_type)

    result = function(*input_numbers)
    print("Result = ", result)
    print("Calculation Done")
    print("")
    write_good_calc()
    done_calc = True

# except ValueError as e:
# print(e)
# write_error(e)
# except ZeroDivisionError as e:
# print(e)
# write_error(e)
#     good_input_y_n = False
#     while not good_input_y_n:
#         another_calculation = input("Do you want to perform another calculation? "
#                                     "(y/n)")
#         if another_calculation == "y":
#             good_input_y_n = True
#
#         elif another_calculation == "n":
#             done_total = True
#             good_input_y_n = True



