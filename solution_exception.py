import datetime

done = False
while not done:
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative")
        else:
            current_year = datetime.datetime.now().year
            birth_year = current_year - age
            print(f"You were born in {birth_year}")
            done = True
    except ValueError as e:
        print(e)
        print("Invalid input, please enter a valid age (0 or higher)")