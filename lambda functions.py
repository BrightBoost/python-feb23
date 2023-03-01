square = lambda x: x ** 2
max_lam = lambda x, y: max(x, y)

squared_even_list = lambda l: list((map(square, filter(lambda x: x % 2 == 0, l))))
even_list = lambda l: list(filter(lambda x: x % 2 == 0, l))

upper_string_list = lambda l: list(map(lambda x: x.upper(), l))

# div_by_3_4_list = lambda l: list(filter(lambda x: x % 3 == 0 and x % 4 == 0, l))

div_by_3_4_list = lambda l: [x for x in l if x % 3 == 0 and x % 4 == 0]

num_list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
num_list2 = [0, 15, 27, 37, 4, 55, 76, 72, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
             20]

print(div_by_3_4_list(num_list1))
print(div_by_3_4_list(num_list2))

print(even_list(num_list1))
