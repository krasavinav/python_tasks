'''
Подвиг 3. Вводится натуральное число N (N > 8). Необходимо определить функцию-генератор, которая бы выдавала пароль
длиной N символов из случайных букв, цифр и некоторых других знаков. Для получения последовательности допустимых
символов для генерации паролей в программе импортированы две строки: ascii_lowercase,
ascii_uppercase (см. листинг ниже), на основе которых формируется общий список:

from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
Функция-генератор должна при каждом вызове возвращать новый пароль из случайно выбранных символов chars длиной N и
делать это бесконечно, то есть, вызывать ее можно бесконечное число раз. Сгенерировать случайный индекс indx в
диапазоне [a; b] для символа можно с помощью функции randint модуля random:

import random
random.seed(1)
indx = random.randint(a, b)
Сгенерируйте с помощью этой функции первые пять паролей и выведите их в столбик (каждый с новой строки).
'''

from string import ascii_lowercase, ascii_uppercase
import random

random.seed(1)
N = int(input())


def gen_pass(N):
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    while True:
        pswd = []
        for i in range(N):
            indx = random.randint(0, len(chars) - 1)
            pswd.append(chars[indx])
        yield ''.join(pswd)


gen = gen_pass(N)
for i in range(5):
    print(next(gen))
