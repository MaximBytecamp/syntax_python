# ==============================================================
# Задание 34.1
# Создать классы Cat и Dog с одинаковым методом speak.
# Вызвать метод у разных объектов.
# ==============================================================


class Cat:
    def speak(self):
        print("Мяу")


class Dog:
    def speak(self):
        print("Гав")


animals = [Cat(), Dog()]

for animal in animals:
    animal.speak()


# ==============================================================
# Задание 34.2
# Создать фигуры с одинаковым методом area.
# ==============================================================


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


figures = [Rectangle(3, 4), Square(5)]

print()
for figure in figures:
    print(figure.area())


# ==============================================================
# Задание 34.3
# Написать функцию, которая вызывает метод draw у любого объекта.
# ==============================================================


class Circle:
    def draw(self):
        print("Рисуем круг")


class Triangle:
    def draw(self):
        print("Рисуем треугольник")


def draw_object(obj):
    obj.draw()


print()
draw_object(Circle())
draw_object(Triangle())


# ==============================================================
# Задание 34.4
# Разные классы имеют метод get_price.
# Посчитать общую стоимость.
# ==============================================================


class Product:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price


class Service:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price


items = [Product(100), Service(250)]
total = 0

for item in items:
    total += item.get_price()

print()
print(total)


# ==============================================================
# Задание 34.5
# Переопределить метод info в дочерних классах.
# ==============================================================


class User:
    def info(self):
        print("Пользователь")


class Admin(User):
    def info(self):
        print("Администратор")


class Guest(User):
    def info(self):
        print("Гость")


users = [Admin(), Guest()]

print()
for user in users:
    user.info()


# ==============================================================
# Задание 34.6
# У разных транспортов есть метод move.
# ==============================================================


class Car:
    def move(self):
        print("Едет")


class Plane:
    def move(self):
        print("Летит")


transport = [Car(), Plane()]

print()
for item in transport:
    item.move()


# ==============================================================
# Задание 34.7
# У разных уведомлений есть метод send.
# ==============================================================


class Email:
    def send(self):
        print("Email отправлен")


class Sms:
    def send(self):
        print("SMS отправлено")


messages = [Email(), Sms()]

print()
for message in messages:
    message.send()


# ==============================================================
# Задание 34.8
# У разных файлов есть метод open.
# ==============================================================


class TextFile:
    def open(self):
        print("Открыт текстовый файл")


class ImageFile:
    def open(self):
        print("Открыт файл изображения")


files = [TextFile(), ImageFile()]

print()
for file in files:
    file.open()


# ==============================================================
# Задание 34.9
# Функция печатает описание любого объекта с методом describe.
# ==============================================================


class Book:
    def describe(self):
        return "Книга"


class Movie:
    def describe(self):
        return "Фильм"


def print_description(obj):
    print(obj.describe())


print()
print_description(Book())
print_description(Movie())


# ==============================================================
# Задание 34.10
# Использовать общий метод calculate у разных классов.
# ==============================================================


class Sum:
    def calculate(self, a, b):
        return a + b


class Multiply:
    def calculate(self, a, b):
        return a * b


operations = [Sum(), Multiply()]

print()
for operation in operations:
    print(operation.calculate(3, 4))
