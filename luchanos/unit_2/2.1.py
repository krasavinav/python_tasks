def foo():
    print('Моя функция foo')


def wrapper(f, *args, **kwargs):
    print('моя функция wrapper')
    print('В качестве аргумента передана функция:', f)
    f(*args, **kwargs)


# c = foo
# c()

wrapper(f=foo)
wrapper(f=print)
wrapper(sum, [1, 2, 3, 4])
