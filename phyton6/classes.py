import re
import datetime


class Emploee:
    
    def __init__(this, name, phone, birthday, email, position ) :
        this.__name = name
        this.__phone = phone
        this.__birthday = birthday
        this.__email = email
        this.__position = position
    
    @property
    def name(this):
        return this.__name
    @name.setter
    def name(this, name):
        temp = r"^[A-Za-z]+$"
        if re.match(temp, name):
            this.__name = name
        else:
            print("Имя не соответсвует шаблону\t")

    @property
    def phone(this):
        return this.__phone
    @phone.setter
    def phone(this, phone):
        temp = r"^(\+373\d{7})$"
        if re.match(temp, phone):
            this.__phone = phone
        else:
            print("Номер телефона не соответствует шаблону\t")

    @property
    def birthday(this):
        return this.__birthday
    @name.setter
    def birthday(self, birthday):
        try:
            datetime_obj = datetime.strptime(birthday, "%d.%m.%Y")
            self.__birthday = datetime_obj.strftime("%d.%m.%Y")
        except ValueError:
            print("Дата не соответсвует шаблону. Шаблон: dd.mm.yyyy")

    def get_email(this):
        return this.__email
    def set_email(this, email):
        this.__email = email
    email = property(get_email, set_email)

    def get_position(this):
        return this.__position
    def set_position(this, position):
        temp = r"^[A-Za-z]{4,20}$"
        if re.match(temp, position):
            this.__position = position
        else:
            print("Формат должности не соответсвует шаблону\t")
 
    def calculateAge():
        pass
    def _calculateSalary():
        pass


class HourlyEmployee(Emploee):
    def __init__(this, name, phone, birthday, email, position, hours, rate ):
        super().__init__(name, phone, birthday, email, position)
        this.__hours = hours
        this.__rate = rate

    @property
    def hours(this):
        return this.hours
    @hours.setter
    def hours(this, hours):
        if this.__hours.isdigit():
            this.__hours = hours
        else:
            print("Вы неправильно ввели часы работы")

    
    @property
    def rate(this):
        return this.rate
    @rate.setter
    def rate(this, rate):
        if this.__rate.isdigit():
            this.__rate = rate
        else:
            print("Вы неправильно ввели почасовую ставку\t")

    def calculateSalary(this):
        salary = this.__hours * this.__rate
        return salary
    
class SalaryEmployee(Emploee):

    def __init__(self, name, phone, birthday, email, position, monthly_salary):
        super().__init__(name, phone, birthday, email, position)
        self.__monthly_salary = monthly_salary

    @property
    def monthly_salary(self):
        return self.__monthly_salary
    @monthly_salary.setter
    def monthly_salary(self, monthly_salary):
        self.__monthly_salary = monthly_salary

    def calculateSalary(self):
        return self.__monthly_salary