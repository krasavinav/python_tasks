# class Money:
#     def __init__(self, money):
#         self.money = money
#
# my_money = Money(100)
# your_money = Money(1000)
###############################################################################################
# class Point:
#     def __init__(self, x, y, color='black'):
#         self.x = x
#         self.y = y
#         self.color = color
#
#
# points = [Point(i, i) if i != 3 else Point(i, i, color='yelow') for i in range(1, 2000, 2)]
# print(points[1].color)
###############################################################################################
# import random
#
#
# class Line:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Rect:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Ellipse:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# elements = []
# for i in range(217):
#     a = random.randint(0, 9)
#     b = random.randint(0, 9)
#     c = random.randint(0, 9)
#     d = random.randint(0, 9)
#     elements.append(random.choice([Line(0, 0, 0, 0), Rect(a, b, c, d), Ellipse(a, b, c, d)]))
#
# print(elements[2])
###############################################################################################
# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if any(type(i) not in (float, int) for i in (self.a, self.b, self.c)) or any(i <= 0 for i in (self.a, self.b, self.c)):
#             self.result = 1
#         elif (self.a + self.b < self.c) or (self.b + self.c < self.a) or (self.c + self.a < self.b):
#             self.result = 2
#         else:
#             self.result = 3
#
#         return self.result
#
#
# a, b, c = (3, '3', 5)
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())
#####################################################################################################
# class Graph:
#
#     def __init__(self, data):
#         self.set_show(True)
#         self.set_data(data)
#
#     def set_data(self, data):
#         self.data = data[:]
#
#     def list_to_str(self):
#         return ' '.join(map(str, self.data))
#
#     def _check_flag(func):
#         def wrapper(self):
#             func(self) if self.is_show else print('Отображение данных закрыто')
#
#         return wrapper
#
#     @_check_flag
#     def show_table(self):
#         print(self.list_to_str())
#
#     @_check_flag
#     def show_graph(self):
#         print('Графическое отображение данных: ', self.list_to_str())
#
#     @_check_flag
#     def show_bar(self):
#         print("Столбчатая диаграмма:", self.list_to_str())
#
#     def set_show(self, fl_show):
#         self.is_show = fl_show
#
#
# # data_graph = list(map(int, input().split()))
# data_graph = [8, 11, 10, -32, 0, 7, 18]
# gr = Graph(data_graph)
# gr.show_bar()
# gr.set_show(fl_show=False)
# gr.show_table()
######################################################################################################
# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr
#
#
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
#
# class MotherBoard:
#     def __init__(self, name, cpu, *args):
#         self.name = name
#         self.cpu = cpu
#         self.total_mem_slots = 4
#         self.mem_slots = list(args)
#
#     def get_config(self):
#         info = [f'Материнская плата: {self.name}',
#                 f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
#                 f'Слотов памяти: {self.total_mem_slots}',
#                 'Память: ' + '; '.join([f'{i.name} - {i.volume}' for i in self.mem_slots[:self.total_mem_slots]])]
#         return info
#
#
# cpu = CPU('Intel Core i7', '1600 MHz')
# mem1 = Memory('DDR3', '4gb')
# mem2 = Memory('DDR3', '4gb')
# mb = MotherBoard('GigabyteTech', cpu, mem1, mem2)
# print(mb.get_config())
#########################################################################################################
# class Cart:
#
#     def __init__(self):
#         self.goods = []
#
#     def add(self, gd):
#         self.goods.append(gd)
#
#     def remove(self, indx):
#         del self.goods[indx]
#
#     def get_list(self):
#         return [f'{i.name}: {i.price}' for i in self.goods]
#
#
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class TV:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Notebook:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Cup:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# cart = Cart()
# tv1 = TV('LG', 'fg212-1')
# cart.add(tv1)
# tv2 = TV('Samsung', 'std112')
# cart.add(tv2)
# tbl1 = Table('директор', 'золотой трон111')
# cart.add(tbl1)
# nb1 = Notebook('lenovo', 'za123')
# cart.add(nb1)
# nb2 = Notebook('asus', 'asd123a')
# cart.add(nb2)
# cp1 = Cup('гжель', 'фарфор')
# cart.add(cp1)
# print(cart.get_list())
######################################################################################################
# class ListObject:
#
#     def __init__(self, data):
#         self.data = data
#         self.next_obj = None
#
#     def link(self, obj):
#         self.next_obj = obj
#
#
# lst_in = ['1. Первые шаги в ООП', '1.1 Как правильно проходить этот курс', '1.2 Концепция ООП простыми словами',
#           '1.3 Классы и объекты. Атрибуты классов и объектов', '1.4 Методы классов. Параметр self',
#           '1.5 Инициализатор init и финализатор del', '1.6 Магический метод new. Пример паттерна Singleton',
#           '1.7 Методы класса (classmethod) и статические методы (staticmethod)']
#
# head_obj = ListObject(lst_in[0])
# obj = head_obj
# for i in range(1, len(lst_in)):
#     new_obj = ListObject(lst_in[i])
#     obj.link(new_obj)
#     obj = new_obj
######################################################################################################
