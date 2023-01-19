class countdown_iterator:
    def __init__(self, num):
        self.num = num
        self.counter = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < 0:
            raise StopIteration
        num_to_return = self.counter
        self.counter -= 1
        return num_to_return


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
