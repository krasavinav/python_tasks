"""
Перенесите глобальный счетчик на уровень объемлющей функции. Будет ли работать наш код? Если да, то как поменялся смысл
написанного кода? Если нет, то что надо изменить, чтобы всё заработало?
"""

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


def wrapper():
    global counter
    counter += 1
    print('мой счетчик', counter)

    def sum_(a, b):
        return a + b

    return sum_
"""
значение глобального счетчика изменяться не будет, т.к. в дальнейшем мы вызываем только внутреннюю функцию через ссылку
"""

res = wrapper()
print(res(1, 4))
print(res(1, 4))
print(res(1, 4))
