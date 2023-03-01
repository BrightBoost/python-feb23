square = lambda x: x ** 2
max_lam = lambda x,y: max(x,y)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
text = ["test", "nog een keer"]

squared_even_numbers = [x**2 for x in numbers if x % 2 == 0]
print(squared_even_numbers)

even_numbers = lambda l: list(filter(lambda x: x % 2 == 0, l))
print(even_numbers(numbers))

upper_case = lambda l:list(map(lambda x: x.upper(), l))
print(upper_case(text))
