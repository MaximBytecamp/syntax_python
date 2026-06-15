# ==============================================================
# Задание 28.1
# Создать класс Person с методом say_hello.
# ==============================================================


class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Привет, меня зовут", self.name)


person = Person("Анна")
person.say_hello()


# ==============================================================
# Задание 28.2
# Создать класс Rectangle с методом area.
# ==============================================================


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(10, 5)

print()
print(rectangle.area())


# ==============================================================
# Задание 28.3
# Создать класс Circle с методом circumference.
# ==============================================================


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14 * self.radius


circle = Circle(5)

print()
print(circle.circumference())


# ==============================================================
# Задание 28.4
# Создать класс Student с методом average_grade.
# ==============================================================


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Иван", [4, 5, 3])

print()
print(student.average_grade())


# ==============================================================
# Задание 28.5
# Создать класс BankAccount с методами deposit и withdraw.
# ==============================================================


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)

print()
print(account.balance)


# ==============================================================
# Задание 28.6
# Создать класс Counter с методами increase и reset.
# ==============================================================


class Counter:
    def __init__(self):
        self.value = 0

    def increase(self):
        self.value += 1

    def reset(self):
        self.value = 0


counter = Counter()
counter.increase()
counter.increase()
counter.reset()

print()
print(counter.value)


# ==============================================================
# Задание 28.7
# Создать класс Product с методом total_price.
# ==============================================================


class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def total_price(self):
        return self.price * self.count


product = Product("молоко", 95, 2)

print()
print(product.total_price())


# ==============================================================
# Задание 28.8
# Создать класс Car с методом drive.
# Метод увеличивает пробег.
# ==============================================================


class Car:
    def __init__(self, mileage):
        self.mileage = mileage

    def drive(self, distance):
        self.mileage += distance


car = Car(10000)
car.drive(150)

print()
print(car.mileage)


# ==============================================================
# Задание 28.9
# Создать класс TodoList с методами add_task и show_tasks.
# ==============================================================


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        for task in self.tasks:
            print(task)


todo = TodoList()
todo.add_task("выучить классы")
todo.add_task("решить задачу")

print()
todo.show_tasks()


# ==============================================================
# Задание 28.10
# Создать класс TextAnalyzer с методом count_words.
# ==============================================================


class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        return len(self.text.split())


analyzer = TextAnalyzer("я изучаю python")

print()
print(analyzer.count_words())
