# ==============================================================
# Задание 36.1
# Создать классы Engine и Car.
# Машина сама создает двигатель внутри конструктора.
# ==============================================================


class Engine:
    def __init__(self):
        self.power = 150


class Car:
    def __init__(self):
        self.engine = Engine()


car = Car()
print(car.engine.power)


# ==============================================================
# Задание 36.2
# Создать классы Passport и Person.
# Человек сам создает паспорт.
# ==============================================================


class Passport:
    def __init__(self, number):
        self.number = number


class Person:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport = Passport(passport_number)


person = Person("Анна", "1234")

print()
print(person.name, person.passport.number)


# ==============================================================
# Задание 36.3
# Создать классы Page и Notebook.
# Блокнот сам создает страницы.
# ==============================================================


class Page:
    def __init__(self, text):
        self.text = text


class Notebook:
    def __init__(self):
        self.pages = [Page("первая"), Page("вторая")]


notebook = Notebook()

print()
print(notebook.pages[0].text)


# ==============================================================
# Задание 36.4
# Создать классы Wheel и Bicycle.
# Велосипед сам создает два колеса.
# ==============================================================


class Wheel:
    def __init__(self, size):
        self.size = size


class Bicycle:
    def __init__(self):
        self.wheels = [Wheel(26), Wheel(26)]


bicycle = Bicycle()

print()
print(len(bicycle.wheels))


# ==============================================================
# Задание 36.5
# Создать классы Keyboard и Computer.
# Компьютер сам создает клавиатуру.
# ==============================================================


class Keyboard:
    def __init__(self):
        self.language = "ru"


class Computer:
    def __init__(self):
        self.keyboard = Keyboard()


computer = Computer()

print()
print(computer.keyboard.language)


# ==============================================================
# Задание 36.6
# Создать классы Battery и Phone.
# Телефон сам создает батарею.
# ==============================================================


class Battery:
    def __init__(self):
        self.charge = 100


class Phone:
    def __init__(self):
        self.battery = Battery()


phone = Phone()

print()
print(phone.battery.charge)


# ==============================================================
# Задание 36.7
# Создать классы Address и User.
# Пользователь сам создает адрес из города и улицы.
# ==============================================================


class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street


class User:
    def __init__(self, name, city, street):
        self.name = name
        self.address = Address(city, street)


user = User("Иван", "Казань", "Ленина")

print()
print(user.address.city, user.address.street)


# ==============================================================
# Задание 36.8
# Создать классы Item и Bag.
# Сумка сама создает пустой список предметов.
# ==============================================================


class Item:
    def __init__(self, name):
        self.name = name


class Bag:
    def __init__(self):
        self.items = []

    def add_item(self, name):
        self.items.append(Item(name))


bag = Bag()
bag.add_item("ключи")

print()
print(bag.items[0].name)


# ==============================================================
# Задание 36.9
# Создать классы Header, Body и Page.
# Страница сама создает заголовок и тело.
# ==============================================================


class Header:
    def __init__(self, text):
        self.text = text


class Body:
    def __init__(self, text):
        self.text = text


class Page:
    def __init__(self, title, text):
        self.header = Header(title)
        self.body = Body(text)


page = Page("ООП", "Композиция")

print()
print(page.header.text, page.body.text)


# ==============================================================
# Задание 36.10
# Создать классы AccountHistory и BankAccount.
# Счет сам создает историю операций.
# ==============================================================


class AccountHistory:
    def __init__(self):
        self.operations = []

    def add_operation(self, text):
        self.operations.append(text)


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.history = AccountHistory()

    def deposit(self, amount):
        self.balance += amount
        self.history.add_operation("пополнение")


account = BankAccount()
account.deposit(100)

print()
print(account.balance, account.history.operations)
