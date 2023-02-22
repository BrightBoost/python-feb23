x = input("What number would you want to divide?")
y = input("By what number would you want to divide" + x + "?")

try:
    result = int(x) / int(y)
except ZeroDivisionError:
    print("You cannot divide by 0.")
except ValueError as e:
    print("Make sure to divide numbers.")
except Exception as e:
    print("Oh no!", e.__class__, "was raised.")
finally:
    print("Done!")
