"""
Подвиг 1. Вводятся два списка целых чисел. Необходимо попарно перебрать их элементы и перемножить между собой.
При реализации программы используйте функции zip и map. Выведите на экран первые три значения, используя функцию next.
Значения выводятся в строчку через пробел. (Полагается, что три выходных значения всегда будут присутствовать).
"""
lst_1 = map(int, input().split())
lst_2 = map(int, input().split())
m = map(lambda x: x[0] * x[1], zip(lst_1, lst_2))
for i in range(3):
    print(next(m), end=' ')