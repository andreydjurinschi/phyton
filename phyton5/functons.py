import re
import os

def clear():
    os.system('cls')

def input_info():
    while True:
        try:
            print("Вы выбрали *добавить информацию о сотруднике*")
            choice1 = input('Добавить нового сотрудника?(1) / Выйти из опции(2): ')
            choice1 = int(choice1)
            if choice1 == 1:
                print('Добавим нового сотрудника:')
                pattern_name = r'[a-zA-Z]+(?:-[a-zA-Z]*)?$'
                pattern_surname = r'[a-zA-Z]+(?:-[a-zA-Z]*)?$'
                pattern_sphere = r'[a-zA-Z0-9]+(?: [a-zA-Z0-9]*)?$'
                
                name = input('Введите имя вашего сотрудника: ')
                while not re.match(pattern_name, name):
                    print('Имя сотрудника введено некорректно! Попробуйте снова...')
                    name = input('Введите имя вашего сотрудника: ')
                    
                surname = input('Введите фамилию сотрудника {}: '.format(name))
                while not re.match(pattern_surname, surname):
                    print('Фамилия сотрудника введена некорректно! Попробуйте снова...')
                    surname = input('Введите фамилию сотрудника {}: '.format(name))
                
                sphere = input('Введите отдел сотрудника {} {}: '.format(name, surname))
                while not re.match(pattern_sphere, sphere):
                    print('Отдел сотрудника введен некорректно! Попробуйте снова...')
                    sphere = input('Введите отдел сотрудника {} {}: '.format(name, surname))
                
                kids = input('Введите кол-во детей у данного сотрудника, которые младше 18: ')
                kids = int(kids)
                while not(0 <= kids < 19):
                    print('У сотрудника не может быть мень 0 и больше 19 детей ')
                
                file = open('data.txt', 'a')
                file.write('{}\t{}\t{}\t{}\n'.format(name,surname,sphere,kids))
                file.close()

                print('Сотрудник {} {} из отдела {} успешно добавлен. Кол-во его детей составляет {}. Вся информация добавлена в файл'.format(name, surname, sphere, kids))
            elif choice1 == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print('Ввод должен быть либо (1), либо (2)')

def show_info():
    print("Вы выбрали *показать информацию о сотрудниках*")
    file = open('data.txt', 'r')
    file_elements = file.readlines()
    total_kids = 0
    print('Список сотрудников и их детей: ')
    for i in file_elements:
        list = i.strip().split('\t')
        name = list[0]
        surname = list[1]
        sphere = list[2]
        kids = list[3]
        print('{}, {}, {}'.format(name, surname, kids))
        total_kids += int(kids)
    print('Общее количество детей <= 18 лет = ', total_kids)

def childfree_info():
    childfree_array = []
    file = open('data.txt', 'r')
    file_elements = file.readlines()
    print('Список сотрудников без детей: ')
    for i in file_elements:
        list = i.strip().split('\t')
        name = list[0]
        surname = list[1]
        kids = list[3]
        if kids == '0':
            name_surname = name + ' '+ surname
            childfree_array.append((name_surname))
    print(childfree_array)

def menu():
    while True:
        try:
            print("Меню:")
            print("1. Добавить информацию о сотруднике")
            print("2. Показать информацию о сотрудниках")
            print("3. Показать сотрудников без детей")
            print("4. Выйти из программы")
            choice = int(input('Выберите опцию меню: '))
            if choice == 1:
                clear()
                input_info()
            elif choice == 2:
                clear()
                show_info()
            elif choice == 3:
                clear()
                childfree_info()
            elif choice == 4:
                clear()
                break
            else:
                raise ValueError
        except ValueError:
            print('Некорректный ввод. Наше меню содержит 4 опции (1 - 4).')


            