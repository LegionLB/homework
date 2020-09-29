class User:

    def __init__(self, path, name, age, surname, phone_number):
        self.path = path
        self.name = name
        self.age = age
        self.surname = surname
        self.phone_number = phone_number

    def save_user_info(self): # --Создания файла с информацией о юзере
        f = open(self.path, 'tw', encoding='utf-8')
        f.write('User name - ')
        f.write(self.name)
        f.write('\n')
        f.write('User age - ')
        f.write(self.age)
        f.write('\n')
        f.write('User surname - ')
        f.write(self.surname)
        f.write('\n')
        f.write('User phone number - ')
        f.write(self.phone_number)
        f.close()


class User_create:

    def __init__(self, path):
        self.path = path
#Для читаемости файла он должен иметь вид:
# User name - ...
# User age - ...
# User surname - ...
# User phone number - ...
    def create_user_from(self):  #-- Создание юзера из файла
        f = open(self.path, 'r')
        fd = f.readlines()
        name = fd[0]
        age = fd[1]
        surname = fd[2]
        phone_number = fd[3]
        user_list = list()
        user_dict = {'User': user_list}
        if fd:
            a = ''.join(name)
            a_list_name = a.split('User name - ')
            the_name = 'User name - ' + a_list_name[1]
            #print('User name - ', the_name) ----Проверка

            a = ''.join(age)
            a_list_age = a.split('User age - ')
            the_age = 'User age - ' + a_list_age[1]
            #print('User age - ', the_age)

            a = ''.join(surname)
            a_list_surname = a.split('User surname - ')
            the_surname = 'User surname - ' + a_list_surname[1]
            #print('User surname - ', the_surname)

            a = ''.join(phone_number)
            a_list_phone_number = a.split('User phone number - ')
            the_phone_number = 'User phone number - ' + a_list_phone_number[1]
            #print('User phone number - ', the_phone_number)
            user_list.append(the_name)
            user_list.append(the_age)
            user_list.append(the_surname)
            user_list.append(the_phone_number)

        print(user_dict) #---- вывод юзеров в виде значений в дикте с ключем "юзер"




# a = User(input('Write a path for txt file, or a path for creating a file: '), input('Write your name: '),
#           input('Write your age: '), input('Write your surname: '), input('Write your phone number: '))
# a.save_user_info()

# b = User_create(input('Write a path for txt file: '))
# b.create_user_from()