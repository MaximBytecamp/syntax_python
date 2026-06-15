# ==============================================================
# Задание 40.1
# Создать класс Person с геттером и сеттером для имени.
# ==============================================================


class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


person = Person("Анна")
person.set_name("Мария")

print(person.get_name())


# ==============================================================
# Задание 40.2
# Создать геттер и сеттер для возраста.
# Возраст не может быть отрицательным.
# ==============================================================


class Person:
    def __init__(self, age):
        self.__age = 0
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age


person = Person(20)
person.set_age(-5)

print()
print(person.get_age())


# ==============================================================
# Задание 40.3
# Создать геттер и сеттер для цены.
# Цена не может быть меньше 0.
# ==============================================================


class Product:
    def __init__(self, price):
        self.__price = 0
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price >= 0:
            self.__price = price


product = Product(100)
product.set_price(150)

print()
print(product.get_price())


# ==============================================================
# Задание 40.4
# Использовать property для имени.
# ==============================================================


class User:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


user = User("Иван")
user.name = "Пётр"

print()
print(user.name)


# ==============================================================
# Задание 40.5
# Использовать property для возраста с проверкой.
# ==============================================================


class Student:
    def __init__(self, age):
        self.__age = 0
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value


student = Student(16)
student.age = -10

print()
print(student.age)


# ==============================================================
# Задание 40.6
# Создать свойство только для чтения.
# ==============================================================


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(5)

print()
print(circle.area)


# ==============================================================
# Задание 40.7
# Сеттер должен убирать пробелы в начале и конце строки.
# ==============================================================


class Title:
    def __init__(self, text):
        self.text = text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value.strip()


title = Title("  Python  ")

print()
print(title.text)


# ==============================================================
# Задание 40.8
# Сеттер должен хранить email только если в нем есть @.
# ==============================================================


class Email:
    def __init__(self, address):
        self.__address = ""
        self.address = address

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if "@" in value:
            self.__address = value


email = Email("test@mail.com")
email.address = "wrong"

print()
print(email.address)


# ==============================================================
# Задание 40.9
# Геттер возвращает копию списка, чтобы защитить данные.
# ==============================================================


class GradeBook:
    def __init__(self):
        self.__grades = []

    def add_grade(self, grade):
        self.__grades.append(grade)

    @property
    def grades(self):
        return self.__grades.copy()


grade_book = GradeBook()
grade_book.add_grade(5)
grade_book.add_grade(4)

print()
print(grade_book.grades)


# ==============================================================
# Задание 40.10
# Сеттер пароля принимает только строки длиной не меньше 8.
# ==============================================================


class Account:
    def __init__(self):
        self.__password = ""

    @property
    def password(self):
        return "пароль скрыт"

    @password.setter
    def password(self, value):
        if len(value) >= 8:
            self.__password = value

    def check_password(self, value):
        return self.__password == value


account = Account()
account.password = "qwerty123"

print()
print(account.password)
print(account.check_password("qwerty123"))
