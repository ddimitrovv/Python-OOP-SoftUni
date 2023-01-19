from itertools import permutations


def possible_permutations(numbers):
    for result in permutations(numbers):
        yield list(result)


[print(n) for n in possible_permutations([1, 2, 3])]
