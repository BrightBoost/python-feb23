def get_nr():
    nr = 0
    while True:
        yield nr
        nr += 5


step5 = get_nr()
print(next(step5))
print(next(step5))
