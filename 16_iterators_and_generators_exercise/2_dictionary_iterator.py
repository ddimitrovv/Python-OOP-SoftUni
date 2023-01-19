class dictionary_iter:
    def __init__(self, my_dict):
        self.my_list = list(my_dict.items())
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.my_list):
            raise StopIteration
        value_to_return = self.my_list[self.counter]
        self.counter += 1
        return value_to_return


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
