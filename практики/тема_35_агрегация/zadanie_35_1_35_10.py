# ==============================================================
# Задание 35.1
# Создать классы Engine и Car.
# Машина получает уже созданный двигатель.
# ==============================================================


class Engine:
    def __init__(self, power):
        self.power = power


class Car:
    def __init__(self, engine):
        self.engine = engine


engine = Engine(150)
car = Car(engine)

print(car.engine.power)


# ==============================================================
# Задание 35.2
# Создать классы Student и Group.
# Группа хранит созданных отдельно студентов.
# ==============================================================


class Student:
    def __init__(self, name):
        self.name = name


class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


student = Student("Анна")
group = Group()
group.add_student(student)

print()
print(group.students[0].name)


# ==============================================================
# Задание 35.3
# Создать классы Author и Book.
# Книга хранит ссылку на автора.
# ==============================================================


class Author:
    def __init__(self, name):
        self.name = name


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


author = Author("Гвидо")
book = Book("Python", author)

print()
print(book.author.name)


# ==============================================================
# Задание 35.4
# Создать классы Department и Employee.
# Отдел хранит сотрудников.
# ==============================================================


class Employee:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self, title):
        self.title = title
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)


employee = Employee("Иван")
department = Department("IT")
department.add_employee(employee)

print()
print(department.title, department.employees[0].name)


# ==============================================================
# Задание 35.5
# Создать классы Team и Player.
# Игрок может существовать отдельно от команды.
# ==============================================================


class Player:
    def __init__(self, name):
        self.name = name


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)


player = Player("Олег")
team = Team("Команда")
team.add_player(player)

print()
print(team.players[0].name)


# ==============================================================
# Задание 35.6
# Создать классы Course и Teacher.
# Курс получает преподавателя извне.
# ==============================================================


class Teacher:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher


teacher = Teacher("Мария")
course = Course("Python", teacher)

print()
print(course.title, course.teacher.name)


# ==============================================================
# Задание 35.7
# Создать классы Library и Book.
# Библиотека хранит список книг.
# ==============================================================


class Book:
    def __init__(self, title):
        self.title = title


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)


book = Book("Алгоритмы")
library = Library()
library.add_book(book)

print()
print(library.books[0].title)


# ==============================================================
# Задание 35.8
# Создать классы Order и Product.
# Заказ хранит товары, созданные отдельно.
# ==============================================================


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)


product = Product("хлеб", 60)
order = Order()
order.add_product(product)

print()
print(order.products[0].name)


# ==============================================================
# Задание 35.9
# Создать классы Company и Office.
# Компания хранит офисы.
# ==============================================================


class Office:
    def __init__(self, city):
        self.city = city


class Company:
    def __init__(self, name):
        self.name = name
        self.offices = []

    def add_office(self, office):
        self.offices.append(office)


office = Office("Москва")
company = Company("IT Corp")
company.add_office(office)

print()
print(company.offices[0].city)


# ==============================================================
# Задание 35.10
# Создать классы Playlist и Song.
# Плейлист хранит песни.
# ==============================================================


class Song:
    def __init__(self, title):
        self.title = title


class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)


song = Song("Track 1")
playlist = Playlist()
playlist.add_song(song)

print()
print(playlist.songs[0].title)
