class take_skip:
    def __init__(self, step, count):
        self.count = count
        self.step = step
        self.num = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.count:
            raise StopIteration
        num_to_return = self.num
        self. num += self.step
        self.counter += 1
        return num_to_return


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
