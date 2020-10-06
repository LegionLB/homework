#не работает корректно, непонял как создавать разные версии
import os
import shutil


# C:\Users\Legion\Desktop

class User:

    def __init__(self, name, path, age, surname, phone_number, company):
        self.name = name
        self.path = path
        self.age = age
        self.surname = surname
        self.phone_number = phone_number
        self.company = company

    def create(self):
        creating_path = self.path + '\\' + self.name
        a = creating_path + '\\' + self.name
        c = 0
        b = '.txt'
        try:
            os.mkdir(creating_path)
        except:
            f = open(a + b, 'tw', encoding='utf-8')
            f.write('User name - ' + self.name + '\n')
            f.write('User age - ' + self.age + '\n')
            f.write('User surname - ' + self.surname + '\n')
            f.write('User phone number - ' + self.phone_number + '\n')
            f.write('User company - ' + self.company)
            f.close()

        f = open(a + b, 'tw', encoding='utf-8')
        f.write('User name - ' + self.name + '\n')
        f.write('User age - ' + self.age + '\n')
        f.write('User surname - ' + self.surname + '\n')
        f.write('User phone number - ' + self.phone_number + '\n')
        f.write('User company - ' + self.company)
        f.close()

        while False:
            if os.path.exists(a + b):
                c += 1
                f1 = open(a + str(c) + b, 'tw', encoding='utf-8')
                f1.write('User name - ' + self.name + '\n')
                f1.write('User age - ' + self.age + '\n')
                f1.write('User surname - ' + self.surname + '\n')
                f1.write('User phone number - ' + self.phone_number + '\n')
                f1.write('User company - ' + self.company)
                f1.close()
            break


a = User(input("input name: "), input('Input path: '), input('input age: '), input('input surname: '), input('input '
                                                                                                             'phone number'),
         input('input company: '))
a.create()

#     def __enter__(self):
#         creating_path_check = os.listdir(self.path)
#         creating_path = creating_path_check + self.name
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
#
# with User as file:
#     pass

# a1 = input('input name : ')
# a = os.listdir('C:\\Users\\Legion\\Desktop')
# b = 'C:\\Users\\Legion\\Desktop\\' + a1
# os.mkdir(b)
