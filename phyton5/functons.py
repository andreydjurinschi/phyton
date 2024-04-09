import re
def inputInfo():
    while True:
        surname = input('Введите фамилию сотрудника: ')
        if not re.match(r'[a-Az-Z]+(?:-[a-Az-Z]*$)'):
            raise ValueError('Введите фамилию сотрудника заново...')
            continue
        name = input('Введите имя сотрудника: ')  
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

            
    