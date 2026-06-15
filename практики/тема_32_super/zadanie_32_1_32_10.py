# ==============================================================
# Задание 32.1
# Использовать super для вызова конструктора родителя.
# ==============================================================


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group


student = Student("Анна", "Python")
print(student.name, student.group)


# ==============================================================
# Задание 32.2
# Использовать super для вызова метода родителя.
# ==============================================================


class Animal:
    def speak(self):
        print("Звук")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("Гав")


dog = Dog()

print()
dog.speak()


# ==============================================================
# Задание 32.3
# Класс Employee наследует Person и добавляет зарплату.
# ==============================================================


class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


employee = Employee("Иван", 70000)

print()
print(employee.name, employee.salary)


# ==============================================================
# Задание 32.4
# Класс Rectangle наследует Shape и вызывает метод info родителя.
# ==============================================================


class Shape:
    def info(self):
        print("Это фигура")


class Rectangle(Shape):
    def info(self):
        super().info()
        print("Это прямоугольник")


rectangle = Rectangle()

print()
rectangle.info()


# ==============================================================
# Задание 32.5
# Класс Admin наследует User и добавляет роль.
# ==============================================================


class User:
    def __init__(self, name):
        self.name = name


class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        self.role = "admin"


admin = Admin("Мария")

print()
print(admin.name, admin.role)


# ==============================================================
# Задание 32.6
# Класс ElectricCar наследует Car и добавляет емкость батареи.
# ==============================================================


class Car:
    def __init__(self, brand):
        self.brand = brand


class ElectricCar(Car):
    def __init__(self, brand, battery):
        super().__init__(brand)
        self.battery = battery


car = ElectricCar("Tesla", 75)

print()
print(car.brand, car.battery)


# ==============================================================
# Задание 32.7
# Класс Manager наследует Employee и вызывает метод describe родителя.
# ==============================================================


class Employee:
    def describe(self):
        print("Сотрудник")


class Manager(Employee):
    def describe(self):
        super().describe()
        print("Менеджер")


manager = Manager()

print()
manager.describe()


# ==============================================================
# Задание 32.8
# Использовать super в цепочке из трех классов.
# ==============================================================


class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        super().show()
        print("B")


class C(B):
    def show(self):
        super().show()
        print("C")


obj = C()

print()
obj.show()


# ==============================================================
# Задание 32.9
# Вызвать родительский метод и изменить его результат.
# ==============================================================


class Price:
    def total(self):
        return 100


class DiscountPrice(Price):
    def total(self):
        return super().total() * 0.9


price = DiscountPrice()

print()
print(price.total())


# ==============================================================
# Задание 32.10
# Использовать super при множественном наследовании.
# ==============================================================


class First:
    def show(self):
        print("First")


class Second(First):
    def show(self):
        super().show()
        print("Second")


class Third(Second):
    def show(self):
        super().show()
        print("Third")


third = Third()

print()
third.show()
