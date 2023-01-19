class vowels:
    vowels_list = 'eyuioa'

    def __init__(self, letters):
        self.letters = letters
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):

        while self.idx < len(self.letters):
            if self.letters[self.idx].lower() not in self.vowels_list:
                self.idx += 1
                continue
            value_to_return = self.letters[self.idx]
            self.idx += 1
            return value_to_return
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
