'''
Подвиг 4. Вводится натуральное число N. Используя строки из латинских букв ascii_lowercase и ascii_uppercase:

from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase
задайте функцию-генератор, которая бы возвращала случайно сформированные email-адреса с доменом mail.ru и длиной
в N символов. Например, при N=6, получим адрес: SCrUZo@mail.ru

Для формирования случайного индекса для строки chars используйте функцию randint модуля random:

import random
random.seed(1)
indx = random.randint(0, len(chars)-1)
Функция-генератор должна возвращать бесконечное число таких адресов, то есть, генерировать постоянно. Выведите первые
пять сгенерированных email и выведите их в столбик (каждый с новой строки).

'''

from string import ascii_lowercase, ascii_uppercase
import random

random.seed(1)
N = int(input())
chars = ascii_lowercase + ascii_uppercase


def gen_pass(N):
    while True:
        pswd = []
        for i in range(N):
            indx = random.randint(0, len(chars) - 1)
            pswd.append(chars[indx])
        yield ''.join(pswd) + '@mail.ru'


gen = gen_pass(N)
for i in range(5):
    print(next(gen))
