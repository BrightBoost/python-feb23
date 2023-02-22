def divide(x, y):
    if y != 0:
        return x / y


def ask_input():
    nr1 = input("Geef een nr: ")
    nr2 = input("Geef nog een nr: ")
    if nr1.isnumeric() and nr2.isnumeric():
        nr1 = int(nr1)
        nr2 = int(nr2)
    else:
        return

    print(divide(nr1, nr2))


ask_input()
