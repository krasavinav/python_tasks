"""
Подвиг 6. Вводятся названия городов в одну строчку через пробел. Необходимо определить функцию map, которая бы
возвращала названия городов только длиной более 5 символов. Вместо остальных названий - строку с дефисом ("-").
Сформировать список из полученных значений и отобразить его на экране в одну строчку через пробел.
"""

s = map(lambda x: x if len(x) > 5 else '-', input().split())
print(*s)