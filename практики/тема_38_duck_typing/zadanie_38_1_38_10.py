# ==============================================================
# Задание 38.1
# Функция вызывает метод speak у любого объекта.
# Главное, чтобы такой метод был.
# ==============================================================


class Cat:
    def speak(self):
        print("Мяу")


class Dog:
    def speak(self):
        print("Гав")


def make_sound(obj):
    obj.speak()


make_sound(Cat())
make_sound(Dog())


# ==============================================================
# Задание 38.2
# Функция вызывает метод draw у любого объекта.
# ==============================================================


class Circle:
    def draw(self):
        print("Круг")


class Square:
    def draw(self):
        print("Квадрат")


def draw_shape(shape):
    shape.draw()


print()
draw_shape(Circle())
draw_shape(Square())


# ==============================================================
# Задание 38.3
# Функция считает длину любого объекта, у которого работает len.
# ==============================================================


def show_length(obj):
    print(len(obj))


print()
show_length("python")
show_length([1, 2, 3])


# ==============================================================
# Задание 38.4
# Функция проходит циклом по любому перебираемому объекту.
# ==============================================================


def print_items(items):
    for item in items:
        print(item)


print()
print_items([1, 2, 3])
print_items("abc")


# ==============================================================
# Задание 38.5
# Функция вызывает метод send у любого сообщения.
# ==============================================================


class Email:
    def send(self):
        print("Email отправлен")


class Sms:
    def send(self):
        print("SMS отправлено")


def send_message(message):
    message.send()


print()
send_message(Email())
send_message(Sms())


# ==============================================================
# Задание 38.6
# Функция вызывает метод save у любого хранилища.
# ==============================================================


class FileStorage:
    def save(self, data):
        print("Сохраняем в файл:", data)


class DatabaseStorage:
    def save(self, data):
        print("Сохраняем в базу:", data)


def save_data(storage, data):
    storage.save(data)


print()
save_data(FileStorage(), "text")
save_data(DatabaseStorage(), "text")


# ==============================================================
# Задание 38.7
# Функция вызывает метод area у любой фигуры.
# ==============================================================


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


def print_area(shape):
    print(shape.area())


print()
print_area(Rectangle(3, 4))
print_area(Circle(5))


# ==============================================================
# Задание 38.8
# Функция вызывает метод start у любого устройства.
# ==============================================================


class Computer:
    def start(self):
        print("Компьютер запущен")


class Car:
    def start(self):
        print("Машина запущена")


def start_device(device):
    device.start()


print()
start_device(Computer())
start_device(Car())


# ==============================================================
# Задание 38.9
# Функция добавляет элемент в любой объект с методом append.
# ==============================================================


def add_item(collection, item):
    collection.append(item)


numbers = [1, 2]
words = ["a", "b"]
add_item(numbers, 3)
add_item(words, "c")

print()
print(numbers)
print(words)


# ==============================================================
# Задание 38.10
# Функция вызывает метод close у любого объекта.
# ==============================================================


class Door:
    def close(self):
        print("Дверь закрыта")


class Window:
    def close(self):
        print("Окно закрыто")


def close_object(obj):
    obj.close()


print()
close_object(Door())
close_object(Window())
