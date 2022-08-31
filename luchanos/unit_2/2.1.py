<<<<<<< HEAD
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
=======
"""
Реализовать счетчик, который будет увеличиваться каждый раз, когда у нас осуществляется запуск функции суммирования.
"""


counter = 0

def sum_(a, b):
    global counter
    counter += 1
    return a + b


sum_(1, 2)
print(counter)
sum_(1, 2)
print(counter)
sum_(1, 2)
print(counter)
sum_(1, 2)
print(counter)
>>>>>>> b997063f96ae84c3da0357affff1202d808c1f26
