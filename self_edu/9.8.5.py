"""
Подвиг 5. Определите функцию с именем get_list_dig, которая возвращает список только из числовых значений переданной
ей коллекции (список или кортеж).

Сигнатура функции должна быть, следующей:

def get_list_dig(lst): ...

Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.

P. S. Не забудьте про необходимость различения булевых значений (False, True) от целочисленных.
"""


def get_list_dig(lst):
    return [i for i in lst if type(i) in (int, float)]
