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
