def genrange(x, y):
    num = x
    while num <= y:
        yield num
        num += 1

print(list(genrange(1, 10)))