import datetime
import os
import re

def clear():
    os.system('cls') # в дальнейшем очищать консоль

def write_transactions_to_file(place, tr_type, tr_date, tr_time, tr_amount): # запись транзакции в файл
    print("Записываем данные в ваш файл {}".format(place))
    file = open(place, "a", encoding='utf-8')
    file.write("{}\t{}\t{}\t{}\n".format(tr_type,tr_date,tr_time,tr_amount))
    file.close()

def check_date(tr_date_check):
    try:
        tr_date_format = '%d.%m.%Y'
        tr_date = datetime.datetime.strptime(tr_date_check, tr_date_format)
        date_today = datetime.datetime.today()
        return datetime.datetime(2024, 1, 1) <= tr_date <= date_today
    except ValueError:
        print('\nФормат даты не соответствует шаблону\n')
        return False

def check_time(tr_time_check):
    try:
        tr_time_format = '%H:%M'
        tr_time = datetime.datetime.strptime(tr_time_check, tr_time_format)
        valid = 0 <= tr_time.hour <= 23 and 0 <= tr_time.minute < 60
        return valid
    except ValueError:
        print('Формат времени не соответствует шаблону\n')
        return False

def check_tr_type(tr_type):
    template = (r'^(доход|расход)$')
    if re.match(template, tr_type, re.IGNORECASE):
        return True
    else:
        return False

def check_tr_amount(tr_amount):
    try:
        tr_amount = float(tr_amount)
        return tr_amount > 0
    except ValueError:
        print('Неверная сумма транзакции\n')
        return False

def sum_of_all_transactions(place): # сумма всех транзакций
    total = 0
    file = open(place, "r", encoding='utf-8')
    for line in file:
        get_lines = line.split("\t")
        tr_amount = get_lines[3]
        tr_type = get_lines[0]
        tr_amount = float(tr_amount)
        if tr_type == 'доход':
            total += tr_amount
        else:
            total -= tr_amount
    file.close()
    return total

def most_profitable_transaction(place): # самая прибыльная транзакция
    max_amount = float('-inf')
    most_profitable_transaction = None
    file = open(place, "r", encoding='utf-8')
    for line in file:
        tr_type, tr_date, tr_time, tr_amount = line.split("\t")
        tr_amount = float(tr_amount)
        if tr_type == "доход" and tr_amount > max_amount:
            max_amount = tr_amount
            most_profitable_transaction = (tr_type, tr_date, tr_time, tr_amount)
    file.close()
    return most_profitable_transaction

def most_unprofitable_transaction(place): # самая убыточная транзакция
    min_amount = float('inf')
    most_unprofitable_transaction = None
    file = open(place, "r", encoding='utf-8')
    for line in file:
        tr_type, tr_date, tr_time, tr_amount = line.split("\t")
        tr_amount = float(tr_amount)
        if tr_type == "расход" and tr_amount < min_amount:
            min_amount = tr_amount
            most_unprofitable_transaction = (tr_type, tr_date, tr_time, tr_amount)
    file.close()
    return most_unprofitable_transaction

def menu():
    place = "transactions.txt"

    while True:
        try:
            print("\nМеню:")
            print("1. Запись транзакции в файл")
            print("2. Вывести суммарный баланс")
            print("3. Вывести информацию о самой прибыльной транзакции")
            print("4. Вывести информацию о самой убыточной транзакции")
            print("5. Выход")

            answer = input("Выберите опцию нашего меню: ")
            answer = int(answer)

            if answer == 1:
                clear()
                tr_date = input("Введите дату вашей транзакции (день.месяц.год): ")
                if not check_date(tr_date):
                    print("Недопустимая дата, попробуйте снова... ")
                tr_date = input("Введите дату вашей транзакции (день.месяц.год): ")
                
                tr_time = input("Введите время совершенной транзакции (час:минуты): ")
                if not check_time(tr_time):
                    print("Недопустимое время, попробуйте снова...")
                tr_time = input("Введите время совершенной транзакции (час:минуты): ")

                tr_type = input("Введите тип вашей транзакции (доход / расход): ")
                if not check_tr_type(tr_type):
                    print("Недопустимый тип транзакции, попробуйте снова...")
                tr_type = input("Введите тип вашей транзакции (доход / расход): ")

                tr_amount = input("Введите сумму вашей транзакции: ")
                if not check_tr_amount(tr_amount):
                    print("Недопустимая сумма, попробуйте снова...")
                tr_amount = input("Введите сумму вашей транзакции: ")
                
                write_transactions_to_file(place, tr_type, tr_date, tr_time, tr_amount)
                print("Транзакция успешно записана в файл  {} \n".format(place))
            
            elif answer == 2:
                try:
                    clear()
                    balance = sum_of_all_transactions(place)
                    print("Баланс на данный момент составляет {} местной валюты".format(balance))
                except FileNotFoundError:
                    print("Для начала вам нужно создать транзакцию и записать ее в файл! ")

            elif answer == 3:
                try:
                    clear()
                    profit = most_profitable_transaction(place)

                    if not profit:
                        print("Невозможно найти самую прибыльную транзакцию, скорее всего вы не ввели ни одной транзакции...")
                    else:
                        print("Отчет о самой прибыльной транзакции")
                        print("Тип - {}, Дата - {}, Время - {}, Доход - {} ".format(profit[0],  profit[1], profit[2], profit[3])) 
                except FileNotFoundError:
                    print("Для начала вам нужно создать транзакцию и записать ее в файл! ")
                    
            elif answer == 4:
                try:
                    clear()
                    regress = most_unprofitable_transaction(place)
                    if not regress:
                        print("Невозможно найти самую убыточную транзакцию, скорее всего вы не ввели ни одной транзакции...")
                    else:
                        print("Отчет о самой убыточной транзакции")
                        print("Тип - {}, Дата - {}, Время - {}, Доход - {} ".format(regress[0],  regress[1], regress[2], regress[3]))
                except FileNotFoundError:
                    print("Для начала вам нужно создать транзакцию и записать ее в файл! ")
            
            elif answer == 5:
                clear()
                break
            
        except ValueError:
            print("Нет такого пункта меню...")

if __name__ == "__main__":
    menu()
