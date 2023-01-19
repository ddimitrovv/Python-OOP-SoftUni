class Stack:
    def __init__(self):
        self.data = list()

    # def is_string(self, value):
    #     if not isinstance(value, str):
    #         raise TypeError('Only strings can be appended to Stack')

    def push(self, element):
        # self.is_string(element)
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        rev_data = [x for x in reversed(self.data)]
        output = '[' + ', '.join(rev_data) + ']'
        return output
