# ==============================================================
# Задание 27.1
# Создать класс Person с конструктором __init__.
# ============================================================== 


class Person:
    def __init__(self, name):
        self.name = name


person = Person("Анна")
print(person.name)


# ==============================================================
# Задание 27.2
# Создать класс Dog с именем и возрастом.
# ==============================================================


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog = Dog("Бим", 3)

print()
print(dog.name, dog.age)


# ==============================================================
# Задание 27.3
# Создать класс Book с названием и автором.
# ==============================================================


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


book = Book("Python", "Гвидо")

print()
print(book.title, book.author)


# ==============================================================
# Задание 27.4
# Создать класс Rectangle с шириной и высотой.
# ==============================================================


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


rectangle = Rectangle(10, 5)

print()
print(rectangle.width, rectangle.height)


# ==============================================================
# Задание 27.5
# Создать класс Student с именем и списком оценок.
# ==============================================================


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades


student = Student("Иван", [4, 5, 3])

print()
print(student.name, student.grades)


# ==============================================================
# Задание 27.6
# Создать класс Car с маркой, моделью и годом выпуска.
# ==============================================================


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


car = Car("Toyota", "Camry", 2020)

print()
print(car.brand, car.model, car.year)


# ==============================================================
# Задание 27.7
# Создать класс Product с названием, ценой и количеством.
# ==============================================================


class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


product = Product("хлеб", 60, 3)

print()
print(product.name, product.price, product.count)


# ==============================================================
# Задание 27.8
# Создать класс Point с координатами x и y.
# ==============================================================


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(2, 7)

print()
print(point.x, point.y)


# ==============================================================
# Задание 27.9
# Создать класс User.
# Если роль не передана, использовать роль "user".
# ==============================================================


class User:
    def __init__(self, name, role="user"):
        self.name = name
        self.role = role


user = User("Мария")
admin = User("Пётр", "admin")

print()
print(user.name, user.role)
print(admin.name, admin.role)


# ==============================================================
# Задание 27.10
# Создать класс BankAccount.
# Если баланс не передан, баланс равен 0.
# ==============================================================


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


account = BankAccount("Анна")

print()
print(account.owner, account.balance)
