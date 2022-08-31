# """
# Подвиг 2
# """
# s = input()
# lst = list(map(int, s.split()))
# tp_ = tuple(lst)
# lst.sort()
# tp_lst = tuple(sorted(tp_))
# print(lst)
# print(tp_lst)


# """
# Подвиг 3
# """
# def get_sort(d):
#     res = [d[i] for i in sorted(d.keys(), reverse=True)]
#     return res
#
# dct = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
# x = get_sort(dct)
# print(x)


# """
# Подвиг 4
# """
# s = list(set(map(int, input().split())))
# s.sort(reverse=True)
# print(*s[:4])


# """
# Подвиг 5
# """
# s_1 = sorted(map(int, input().split()))
# s_2 = sorted(map(int, input().split()), reverse=True)
# res = map(lambda x: sum(x), zip(s_1, s_2))
# print(*res)


"""
Подвиг 6
"""


def cheap_price(dct):
    return [d[i] for i in sorted(dct.keys())[:3]]


lst_in = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']
d = {}
for i in lst_in:
    x = i.split(':')
    d[int(x[1])] = x[0]
print(*cheap_price(d))
