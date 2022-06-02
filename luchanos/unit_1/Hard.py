def sum_func(a, b, c, d, *args):
    s = a + b + c + d
    return s


def sum_func1(a, b, c, d, *args):
    s = a + b + c + d + sum(args[:2])
    return s


def sum_func2(a, b, c, d, *args, **kwargs):
    s = a + b + c + d + sum(args) + sum(kwargs)
    return s


f = sum_func
f1 = sum_func1
f2 = sum_func2
print(f(1, 2, 3, 6))
print(f1(1, 1, 1, 1, 1, 1, 2))
print(f2(a = 1, b = 2, c = 3, d = 4, e = 5, f = 6, g = 7))
