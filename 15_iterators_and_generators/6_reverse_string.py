def reverse_text(string):
    index = -1
    while index >= -len(string):
        yield string[index]
        index -= 1


for char in reverse_text("step"):
    print(char, end='')
