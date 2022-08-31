"""
Подвиг 5. Известно, что звания военнослужащих имеют следующий порядок:

рядовой, сержант, старшина, прапорщик, лейтенант, капитан, майор, подполковник, полковник

На вход поступает список военнослужащих в формате:

имя_1=звание_1
...
имя_N=звание_N

Необходимо входные данные представить в виде вложенного списка вида:

[['имя_1', 'звание_1'], ['имя_2', 'звание_2'], ..., ['имя_N', 'звание_N']]

Этот список присвоить переменной с именем lst. Затем, отсортировать его по возрастанию званий.
Выводить на экран ничего не нужно, только сформировать список и указать на него переменную lst.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
"""
lst_in = ['Атос=лейтенант', 'Портос=прапорщик', "д'Артаньян=капитан", 'Арамис=лейтенант', 'Балакирев=рядовой']
zv = 'рядовой, сержант, старшина, прапорщик, лейтенант, капитан, майор, подполковник, полковник'
lst = [[st for st in row.split('=')] for row in lst_in]
lst = sorted(lst, key=lambda x: zv.find(x[1]))
