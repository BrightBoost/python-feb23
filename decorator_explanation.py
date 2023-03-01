def say_hi(name):
    print("Hi", name)


def say_bye(name):
    print("Bye", name)


def greet(func):
    func("Raoul")


def outer(choice):
    def inner1():
        print("In inner function")

    def inner2():
        print("In inner2 function")

    if choice == 1:
        return inner1
    elif choice == 2:
        return inner2
    else:
        return lambda x: x


i1 = outer(1)
i2 = outer(2)

i2()

greet(say_hi)
greet(say_bye)





# create our own decorator function (without decorator notation)
def boop_decorator(func):
    def wrap_func_in_boop():
        print("boop")
        func()
        print("boop")
    return wrap_func_in_boop


@boop_decorator # same as: hi = boop_decorator(hi)
def hi():
    print("hi")


hi()
