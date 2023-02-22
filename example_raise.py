def ask_nr():
    x = input("wat is je nr? ")
    if not x.isnumeric():
        raise TypeError
    x = int(x)
    print(x * 4)


ask_nr()
