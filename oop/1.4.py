# class MediaPlayer:
#
#     def open(self, file):
#         self.filename = file
#
#     def play(self):
#         print(f'Воспроизведение {self.filename}')
#
#
# media1 = MediaPlayer()
# media2 = MediaPlayer()
# media1.open('filemedia1')
# media2.open('filemedia2')
# media1.play()
# media2.play()
###################################################################################################
# class Graph:
#     LIMIT_Y = [0, 10]
#
#     def set_data(self, data):
#         self.data = data
#
#     def draw(self):
#         for i in self.data:
#             if Graph.LIMIT_Y[0] <= i <= Graph.LIMIT_Y[-1]:
#                 print(i, end=' ')
#
#
# lst = [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]
# graph_1 = Graph()
# graph_1.set_data(lst)
# graph_1.draw()
###################################################################################################
# import sys
#
#
# class StreamData:
#
#     def create(self, fields, lst_values):
#         if len(fields) != len(lst_values):
#             return False
#         else:
#             for i, y in zip(fields, lst_values):
#                 setattr(self, i, y)
#             return True
#
#
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         # lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         lst_in = [10, 'Gbnjy', 500]
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
#
#
# sr = StreamReader()
# data, result = sr.readlines()
# print(data.__dict__)
# print(result)
###################################################################################################
# import sys
#
# # программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#
#
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     def select(self, a, b):
#         return self.lst_data[a: b + 1]
#
#     def insert(self, data):
#         for i in data:
#             self.lst_data.append(dict(zip(self.FIELDS, i.split())))
#         # print(self.lst_data)
#
#
# db = DataBase()
# db.insert(lst_in)
#
# print(db.select(1, 10))
###################################################################################################
class Translator:

    def add(self, eng, rus):
        if 'dct' not in self.__dict__:
            self.dct = {}

        self.dct.setdefault(eng, [])
        if rus not in self.dct[eng]:
            self.dct[eng].append(rus)

    def remove(self, eng):
        self.dct.pop(eng, False)

    def translate(self, eng):
        return self.dct[eng]


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
print(tr.dct)
tr.remove('asd')
print(*tr.translate('go'))
