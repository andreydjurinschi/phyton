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
        this.__name = name

    @property
    def phone(this):
        return this.__phone
    @phone.setter
    def phone(this, phone):
        this.__phone = phone

    @property
    def birthday(this):
        return this.__birthday
    @name.setter
    def name(this, birthday):
        this.__birthday = birthday

    def get_email(this):
        return this.__email
    def set_email(this, email):
        this.__email = email
    email = property(get_email, set_email)

    def get_position(this):
        return this.__position
    def set_position(this, position):
        this.__position = position

"""Отличие декораторов от функции проперти """
    
    
def calculateAge():
    pass
def _calculateSalary():
    pass

class HourlyEmployee(Emploee):
    