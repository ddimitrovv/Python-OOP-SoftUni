# Fix the code below, so it returns the expected output. Submit the fixed code in the judge system.
# x = "global"
#
#
# def outer():
#     x = "local"
#
#     def inner():
#         x = "nonlocal"
#         print("inner:", x)
#
#     def change_global():
#         x = "global: changed!"
#
#     print("outer:", x)
#     inner()
#     print("outer:", x)
#     change_global()
#
#
# print(x)
# outer()
# print(x)

x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)
