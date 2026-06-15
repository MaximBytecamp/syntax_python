# ==============================================================
# Задание 31.1
# Создать базовый класс Animal и класс Dog-наследник.
# ==============================================================


class Animal:
    def eat(self):
        print("Животное ест")


class Dog(Animal):
    pass


dog = Dog()
dog.eat()


# ==============================================================
# Задание 31.2
# Создать класс Cat, который наследует метод sleep от Animal.
# ==============================================================


class Animal:
    def sleep(self):
        print("Спит")


class Cat(Animal):
    pass


cat = Cat()

print()
cat.sleep()


# ==============================================================
# Задание 31.3
# Создать класс Car от Vehicle.
# Добавить метод drive в дочерний класс.
# ==============================================================


class Vehicle:
    def start(self):
        print("Транспорт запущен")


class Car(Vehicle):
    def drive(self):
        print("Машина едет")


car = Car()

print()
car.start()
car.drive()


# ==============================================================
# Задание 31.4
# Создать класс Student от Person.
# Студент наследует имя и имеет свою группу.
# ==============================================================


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def set_group(self, group):
        self.group = group


student = Student("Анна")
student.set_group("Python")

print()
print(student.name, student.group)


# ==============================================================
# Задание 31.5
# Переопределить метод speak в дочернем классе.
# ==============================================================


class Animal:
    def speak(self):
        print("Звук")


class Dog(Animal):
    def speak(self):
        print("Гав")


dog = Dog()

print()
dog.speak()


# ==============================================================
# Задание 31.6
# Создать классы Shape и Rectangle.
# Rectangle переопределяет метод area.
# ==============================================================


class Shape:
    def area(self):
        return 0


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
# Задание 31.7
# Создать класс Admin от User.
# Admin получает метод ban_user.
# ==============================================================


class User:
    def __init__(self, name):
        self.name = name


class Admin(User):
    def ban_user(self, user):
        print(self.name, "заблокировал", user.name)


admin = Admin("Олег")
user = User("Иван")

print()
admin.ban_user(user)


# ==============================================================
# Задание 31.8
# Создать класс ElectricCar от Car.
# Электромобиль наследует марку.
# ==============================================================


class Car:
    def __init__(self, brand):
        self.brand = brand


class ElectricCar(Car):
    def charge(self):
        print("Зарядка")


electric_car = ElectricCar("Tesla")

print()
print(electric_car.brand)
electric_car.charge()


# ==============================================================
# Задание 31.9
# Проверить, является ли объект экземпляром базового класса.
# ==============================================================


class Animal:
    pass


class Cat(Animal):
    pass


cat = Cat()

print()
print(isinstance(cat, Animal))


# ==============================================================
# Задание 31.10
# Проверить, является ли класс наследником другого класса.
# ==============================================================


class Worker:
    pass


class Programmer(Worker):
    pass


print()
print(issubclass(Programmer, Worker))
