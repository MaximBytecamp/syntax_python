from abc import ABC, abstractmethod


# ==============================================================
# Задание 39.1
# Создать абстрактный класс Animal с методом speak.
# ==============================================================


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Гав")


dog = Dog()
dog.speak()


# ==============================================================
# Задание 39.2
# Создать абстрактный класс Shape с методом area.
# ==============================================================


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(4, 5)

print()
print(rectangle.area())


# ==============================================================
# Задание 39.3
# Создать абстрактный класс Transport с методом move.
# ==============================================================


class Transport(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Transport):
    def move(self):
        print("Едет")


car = Car()

print()
car.move()


# ==============================================================
# Задание 39.4
# Создать абстрактный класс Notification с методом send.
# ==============================================================


class Notification(ABC):
    @abstractmethod
    def send(self):
        pass


class Email(Notification):
    def send(self):
        print("Email отправлен")


email = Email()

print()
email.send()


# ==============================================================
# Задание 39.5
# Создать абстрактный класс Storage с методом save.
# ==============================================================


class Storage(ABC):
    @abstractmethod
    def save(self, data):
        pass


class FileStorage(Storage):
    def save(self, data):
        print("Файл:", data)


storage = FileStorage()

print()
storage.save("text")


# ==============================================================
# Задание 39.6
# Создать абстрактный класс Payment с методом pay.
# ==============================================================


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        print("Оплата картой:", amount)


payment = CardPayment()

print()
payment.pay(500)


# ==============================================================
# Задание 39.7
# Создать абстрактный класс Parser с методом parse.
# ==============================================================


class Parser(ABC):
    @abstractmethod
    def parse(self, text):
        pass


class WordParser(Parser):
    def parse(self, text):
        return text.split()


parser = WordParser()

print()
print(parser.parse("я изучаю python"))


# ==============================================================
# Задание 39.8
# Создать абстрактный класс Report с методом build.
# ==============================================================


class Report(ABC):
    @abstractmethod
    def build(self):
        pass


class TextReport(Report):
    def build(self):
        return "Отчет готов"


report = TextReport()

print()
print(report.build())


# ==============================================================
# Задание 39.9
# Абстрактный класс может иметь обычный метод.
# ==============================================================


class BaseWorker(ABC):
    def info(self):
        print("Работник")

    @abstractmethod
    def work(self):
        pass


class Programmer(BaseWorker):
    def work(self):
        print("Пишет код")


programmer = Programmer()

print()
programmer.info()
programmer.work()


# ==============================================================
# Задание 39.10
# Создать список объектов, реализующих один абстрактный метод.
# ==============================================================


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class PrintCommand(Command):
    def execute(self):
        print("Печать")


class SaveCommand(Command):
    def execute(self):
        print("Сохранение")


commands = [PrintCommand(), SaveCommand()]

print()
for command in commands:
    command.execute()
