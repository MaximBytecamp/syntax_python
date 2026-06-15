# ==============================================================
# Задание 37.1
# Создать класс BankAccount с приватным балансом.
# ============================================================== 


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print(self.__balance)


account = BankAccount(1000)
account.show_balance()


# ==============================================================
# Задание 37.2
# Изменять приватный баланс только через метод deposit.
# ==============================================================


class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount()
account.deposit(500)

print()
print(account.get_balance())


# ==============================================================
# Задание 37.3
# Создать класс User с приватным паролем.
# ==============================================================


class User:
    def __init__(self, login, password):
        self.login = login
        self.__password = password

    def check_password(self, password):
        return self.__password == password


user = User("admin", "12345")

print()
print(user.check_password("12345"))


# ==============================================================
# Задание 37.4
# Создать защищенное поле _name.
# ============================================================== 


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


person = Person("Анна")

print()
print(person.get_name())


# ==============================================================
# Задание 37.5
# Запретить отрицательный возраст через метод set_age.
# ==============================================================


class Person:
    def __init__(self, age):
        self.__age = 0
        self.set_age(age)

    def set_age(self, age):
        if age >= 0:
            self.__age = age

    def get_age(self):
        return self.__age


person = Person(20)
person.set_age(-5)

print()
print(person.get_age())


# ==============================================================
# Задание 37.6
# Создать класс Product с приватной ценой.
# Цена не может быть меньше 0.
# ==============================================================


class Product:
    def __init__(self, price):
        self.__price = 0
        self.set_price(price)

    def set_price(self, price):
        if price >= 0:
            self.__price = price

    def get_price(self):
        return self.__price


product = Product(100)
product.set_price(-10)

print()
print(product.get_price())


# ==============================================================
# Задание 37.7
# Скрыть список оценок и добавлять оценки через метод.
# ==============================================================


class Student:
    def __init__(self, name):
        self.name = name
        self.__grades = []

    def add_grade(self, grade):
        if 1 <= grade <= 5:
            self.__grades.append(grade)

    def average(self):
        return sum(self.__grades) / len(self.__grades)


student = Student("Иван")
student.add_grade(5)
student.add_grade(4)

print()
print(student.average())


# ==============================================================
# Задание 37.8
# Скрыть счетчик и увеличивать его только методом increase.
# ==============================================================


class Counter:
    def __init__(self):
        self.__value = 0

    def increase(self):
        self.__value += 1

    def get_value(self):
        return self.__value


counter = Counter()
counter.increase()
counter.increase()

print()
print(counter.get_value())


# ==============================================================
# Задание 37.9
# Создать класс Email с приватным адресом.
# Проверять наличие символа @.
# ==============================================================


class Email:
    def __init__(self, address):
        self.__address = ""
        self.set_address(address)

    def set_address(self, address):
        if "@" in address:
            self.__address = address

    def get_address(self):
        return self.__address


email = Email("test@mail.com")

print()
print(email.get_address())


# ==============================================================
# Задание 37.10
# Создать класс SafeList.
# Список скрыт, добавление идет через метод add.
# ==============================================================


class SafeList:
    def __init__(self):
        self.__items = []

    def add(self, item):
        self.__items.append(item)

    def get_items(self):
        return self.__items.copy()


safe_list = SafeList()
safe_list.add("python")

print()
print(safe_list.get_items())
