import re
def inputInfo():
    while True:
        name = input('Введите имя сотрудника: ')  
        if not re.match(r'[a-Az-Z]+(?:-[a-Az-Z]*$)'):
            raise ValueError('Введите фамилию сотрудника заново...')
            continue  
        surname = input('Введите фамилию сотрудника: ')
        if not re.match(r'[a-Az-Z]+(?:-[a-Az-Z]*$)'):
            raise ValueError('Введите фамилию сотрудника заново...')
            continue

        branch = input('Введите отдел, в котором работает сотрудник: ')
        if not re.match(r'[a-Az-Z0-9]+$)'):
            raise ValueError('Введите отдел сотрудника заново...')
            continue
        kids = input('Введите кол-во детей у сотрудника')
        if not kids.isdigit() or not (0 <= kids <= 19):
            raise ('Кол-во детей должно отображаться в целых числах от 0 до 19...')
            continue
        with open('info.txt', 'a') as file:
            file.write('{}\t{}\t{}\t{}\n'.format(name, surname, branch, kids))

def showInfo():
    totalKids = 0
    with open('info.txt', 'r') as file:
        for employer_info in file:
            part = employer_info.strip().split('\t')
            name = part[0]
            surname = part[1]
            branch = part[2]
            kids = part[3]
            print('Информация о сотрудниках: Имя: {} Фамилия: {} Отдел {} Кол-во детей{}'.format(name, surname, branch, kids))        
            totalKids += int(kids)
        print('Всего детей у сотрудников - {}'.format(totalKids))
        return totalKids

def noChild():
    childness_array = []
    with open('info.txt', 'r') as file:
        for employer_info in file:
            part = employer_info.strip().split('\t')
            name = part[0]
            surname = part[1]
            kids = part[3]
            if(kids == '0'):
                childness_array.append((name,surname))
    if  childness_array:
        print('Бездетные сотрудники:')
        print(childness_array)
    else:
        print('Бездетных сотрудников нет')

def main():
    while True:
        print('Меню:')
        print('1) Введите информацию о сотруднике:')
        print('2) Вывести информацию о сотрудниках и общем кол-ве всех детей:')
        print('3) Вывести сотрудников у которых нет детей:')
        print('4) Выход...')
        answer = input 
    