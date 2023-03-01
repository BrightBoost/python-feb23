import calc


def get_input_calculation():
    done = False
    operation = ""
    nums = []
    while not done:
        operation = input("What operation would you like to perform? (+, *, -, /): ")
        if operation not in ["+", "*", "-", "/"]:
            print("Invalid operation")
            continue
        nums = input("Enter the numbers to perform the operation on (separated by spaces): ")
        try:
            nums = [float(num) for num in nums.split()]
        except ValueError:
            print("Invalid input")
            continue
        if operation in ["-", "/"] and len(nums) != 2:
            print(f"{operation} requires exactly two numbers")
            continue
        elif operation == "*" and len(nums) < 2:
            print(f"{operation} requires at least two numbers")
            continue
        done = True
    return operation, nums


def perform_calculation(operation, nums):
    if operation == "+":
        result = calc.add(*nums)
    elif operation == "*":
        result = calc.multiply(*nums)
    elif operation == "-":
        result = calc.subtract(*nums)
    elif operation == "/":
        result = calc.divide(*nums)
    return result


def write_successful_calculation(operation, nums, result, file):
    file.write(f"{operation} {nums} = {result}\n")
    print(f"{operation} {nums} = {result}")


def write_failed_calculation(operation, nums, file):
    file.write(f"{operation} {nums}\n")
    print(f"Cannot perform {operation} on {nums}, dividing by zero")


def main():
    successful_calculations_file = open("successful_calculations.txt", "a")
    failed_calculations_file = open("failed_calculations.txt", "a")

    while True:
        operation, nums = get_input_calculation()
        result = perform_calculation(operation, nums)
        if result is None:
            write_failed_calculation(operation, nums, failed_calculations_file)
        else:
            write_successful_calculation(operation, nums, result, successful_calculations_file)
        repeat = input("Do you want to perform another calculation? (Y/N): ")
        if repeat.upper() != "Y":
            break

    successful_calculations_file.close()
    failed_calculations_file.close()


if __name__ == "__main__":
    main()
