# Create a program that reads a positive integer N as input
# and prints on the console a rhombus with size n:

def rhombus():
    n = int(input())
    for i in range(n):
        spaces = n - i - 1
        stars = i + 1
        print(spaces * ' ' + stars * ' *')
    for i in range(n - 2, -1, -1):
        spaces = n - i - 1
        stars = i + 1
        print(spaces * ' ' + stars * ' *')


rhombus()
