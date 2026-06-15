# ==============================================================
# Задание 30.1
# Создать классы Author и Book.
# Книга хранит автора.
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

print(book.title, book.author.name)


# ==============================================================
# Задание 30.2
# Создать классы Student и Group.
# Группа хранит список студентов.
# ==============================================================


class Student:
    def __init__(self, name):
        self.name = name


class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


group = Group("Python")
group.add_student(Student("Анна"))
group.add_student(Student("Иван"))

print()
for student in group.students:
    print(student.name)


# ==============================================================
# Задание 30.3
# Создать классы Product и Cart.
# Корзина считает общую стоимость товаров.
# ==============================================================


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        return sum(product.price for product in self.products)


cart = Cart()
cart.add_product(Product("хлеб", 60))
cart.add_product(Product("молоко", 95))

print()
print(cart.total_price())


# ==============================================================
# Задание 30.4
# Создать классы Engine и Car.
# Машина хранит двигатель.
# ==============================================================


class Engine:
    def __init__(self, power):
        self.power = power


class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine


engine = Engine(150)
car = Car("Toyota", engine)

print()
print(car.brand, car.engine.power)


# ==============================================================
# Задание 30.5
# Создать классы Address и User.
# Пользователь хранит адрес.
# ==============================================================


class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street


class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address


user = User("Мария", Address("Казань", "Ленина"))

print()
print(user.name, user.address.city, user.address.street)


# ==============================================================
# Задание 30.6
# Создать классы Teacher, Course.
# Курс хранит преподавателя.
# ==============================================================


class Teacher:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher


course = Course("Python", Teacher("Олег"))

print()
print(course.title, course.teacher.name)


# ==============================================================
# Задание 30.7
# Создать классы Player и Team.
# Команда хранит игроков.
# ==============================================================


class Player:
    def __init__(self, name):
        self.name = name


class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)


team = Team()
team.add_player(Player("Игорь"))
team.add_player(Player("Павел"))

print()
for player in team.players:
    print(player.name)


# ==============================================================
# Задание 30.8
# Создать классы Question и Test.
# Тест хранит вопросы.
# ==============================================================


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class Test:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)


test = Test()
test.add_question(Question("2 + 2?", "4"))

print()
print(test.questions[0].text, test.questions[0].answer)


# ==============================================================
# Задание 30.9
# Создать классы OrderItem и Order.
# Заказ считает сумму по позициям.
# ==============================================================


class OrderItem:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def total(self):
        return self.price * self.count


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total(self):
        return sum(item.total() for item in self.items)


order = Order()
order.add_item(OrderItem("сыр", 320, 2))
order.add_item(OrderItem("хлеб", 60, 1))

print()
print(order.total())


# ==============================================================
# Задание 30.10
# Создать классы Comment и Post.
# Пост хранит комментарии.
# ==============================================================


class Comment:
    def __init__(self, text):
        self.text = text


class Post:
    def __init__(self, title):
        self.title = title
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)


post = Post("ООП")
post.add_comment(Comment("полезно"))

print()
print(post.title, post.comments[0].text)
