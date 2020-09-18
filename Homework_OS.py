import os
#a = "D:/Testpy"
#b = "D:/Testpy/txt(имя создаваемой папки)"
class Transport:
    def __init__(self, transport_from, transport_to, transport_what):
        self.transport_from = transport_from
        self.transport_to = transport_to
        self.transport_what = transport_what


    def to_transport(self):
        d = os.listdir(self.transport_from)
        path_start = self.transport_from
        path = self.transport_to
        os.mkdir(path)
        for i in d:
            j = i.split('.')
            if len(j) >= 2:
                if j[-1] == self.transport_what:
                    print(j)
                    j = '.'.join(j)
                    print(j)
                    os.rename(os.path.join(path_start, j), os.path.join(path, j))
                else:
                    pass
            elif len(j) <=1:
                pass


a = Transport(input('Введите путь папки из которой вы хотите переместить: '), input('Введите путь к папке в которую вы хотите переместить: '), input('Введите тип файла который вы хотите переместить: '))
a.to_transport()

# a = os.listdir("D:/Testpy")
# path_start = "D:/Testpy"
# path = "D:/Testpy/txt"
# os.mkdir(path)
# for i in a:
#     j = i.split('.')
#     print(j)
#     if len(j) <= 2:
#         if j[-1] == 'txt':
#             print(j)
#             j = '.'.join(j)
#             print(j)
#             g = os.rename(os.path.join(path_start, j), os.path.join(path, j))
#             print(g)
#         else:
#             pass
#     elif len(j) <=1:
#         pass
