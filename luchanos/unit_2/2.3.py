counter = 0


# def sqrt(num):
#     global counter
#     counter += 1
#     return num ** (1 / 2)


# def wrapper():
#     global counter
#     counter += 1
#
#     def sum_(a, b):
#         print('мой счетчик', counter)
#         return a + b
#
#     return sum_


def wrapper(a, b):
    global counter
    counter += 1

    def sum_():
        print('мой счетчик', counter)
        return a + b

    return sum_

res = wrapper
print(res(1, 4))
print(res(1, 4))
print(res(1, 4))
print(res(1, 4))
print(res(1, 4))
print(res(1, 4))
