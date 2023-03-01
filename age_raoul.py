done = False

while not done:
    try:
        age = input("What is your age?")
        age = int(age)

        if age < 0:
            raise ValueError("Age is negative and that's impossible")

        else:
            birthyear = 2023 - age
            print("Your birthyear is ", birthyear)
            done = True
    except ValueError as e:
        print("value-error")
        print(e)
    except TypeError as e:
        print("type-error")
        print("Dit is geen getal",e)


