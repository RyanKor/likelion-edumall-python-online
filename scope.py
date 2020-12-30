# a = 10


# def function():
#     global a
#     print(a)


# function()
# print(a)


i = 0


def count():
    global i
    i += 1
    return i


for i in range(10):
    print(count())
