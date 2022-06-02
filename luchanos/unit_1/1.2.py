def sum_func(*args):
    return sum(args)


print(sum_func(1, 2, 3, 4, 5, 6, 7, ))


def sum_func2(a, b, c, d, *args):git
    return a + b + c + d + sum(args)


# print(sum_func2(1)) #ошибка, не достает еще 3х аргументов
print(sum_func2(a=1, b=2, c=3, d=4))
tup = 1, 2, 3, 4
print(sum_func2(*tup))
d = dict(a = 1, b = 22, c = 10, d = 14)
#print(sum_func2(*d))
print(sum_func2(**d))