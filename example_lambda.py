def square(x):
    return x**2


def show(x):
    print(x)


def foreach(arr, lam):
    for item in arr:
        lam(item)


fruits = ["banana", "apple", "grape"]
foreach(fruits, show)
foreach(fruits, lambda x: print(x))

lambda_square = lambda x: x**2
print(lambda_square(2))
print(square(3))

lambda_multiply = lambda x, y: x * y
lambda_multiply(3, 5)

nrs = [1, 2, 3, 4, 5]
squared_nrs = list(map(lambda x: x**2, nrs))
print(squared_nrs)

even_nrs = list(filter(lambda x: x % 2 == 0, nrs))
odd_nrs = list(filter(lambda x: x % 2 != 0, nrs))

names = ["zach", "ann", "charly"]
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)
