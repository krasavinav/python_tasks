"""
Подвиг 2. На вход программы подается целое десятичное число. Используя битовые операции, включите третий бит введенного
 числа. Выведите на экран полученное числовое значение.

P. S. Распределение номеров бит представлено на следующем рисунке.

"""

# n = int(input())
# res = n | 8
# print(bin(res))
# print(res)

"""
Подвиг 3. На вход программы подается целое десятичное число. Используя битовые операции, выключите 4-й и 1-й биты
 введенного числа. Выведите на экран полученное числовое значение.

P. S. Распределение номеров бит представлено на следующем рисунке.
"""
# n = int(input())
# res = n & 18
# print(res)

"""
Подвиг 4. На вход программы подается целое десятичное число. Используя битовые операции, переключите 3-й и 0-й биты 
введенного числа. Выведите на экран полученное числовое значение.
"""
# n = int(input())
# res = n >> 1
# print(res)

"""
Подвиг 7. Вводится зашифрованное слово. Шифрование кодов символов этого слова было проведено с помощью битовой операции 
XOR с ключом key=123. То есть, каждый символ был преобразован по алгоритму:

x = ord(x) ^ key

Здесь ord - функция, возвращающая код символа x. Расшифруйте введенное слово и выведите его на экран.

P. S. Подсказка: для преобразования кода в символ используйте функцию chr.
"""
# st_in = input()
# st_out = ''
# key = 123
# for i in st_in:
#     st_out += chr(ord(i) ^ key)
# print(st_out)

"""
Подвиг 8. На вход программы подается целое десятичное число. Используя битовые операции, проверьте, включен ли 
6-й и 3-й биты введенного числа. Если они оба включены, то выведите слово ДА, иначе - слово НЕТ.

P. S. Распределение номеров бит представлено на следующем рисунке.
"""
in_ = int(input())
if in_ | 32 == in_ or in_ | 2 == in_:
    print('ДА')
else:
    print('НЕТ')