class sequence_repeat:
    def __init__(self, sequence, num):
        self.sequence = sequence
        self.num = num
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.num:
            raise StopIteration
        to_return = self.sequence[self.index % len(self.sequence)]
        self.index += 1
        return to_return


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
