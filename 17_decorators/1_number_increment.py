def number_increment(numbers):

    def increase():
        nums = [x + 1 for x in numbers]
        return nums

    return increase()


print(number_increment([1, 2, 3]))
