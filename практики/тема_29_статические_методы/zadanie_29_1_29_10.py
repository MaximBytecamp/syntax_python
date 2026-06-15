# ==============================================================
# Задание 29.1
# Создать статический метод для сложения двух чисел.
# ==============================================================


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(2, 3))


# ==============================================================
# Задание 29.2
# Создать статический метод проверки четности.
# ==============================================================


class NumberUtils:
    @staticmethod
    def is_even(number):
        return number % 2 == 0


print()
print(NumberUtils.is_even(8))


# ==============================================================
# Задание 29.3
# Создать статический метод для поиска максимума из двух чисел.
# ==============================================================


class MathUtils:
    @staticmethod
    def max_two(a, b):
        return a if a > b else b


print()
print(MathUtils.max_two(10, 15))


# ==============================================================
# Задание 29.4
# Создать статический метод для перевода строки в верхний регистр.
# ==============================================================


class StringUtils:
    @staticmethod
    def to_upper(text):
        return text.upper()


print()
print(StringUtils.to_upper("python"))


# ==============================================================
# Задание 29.5
# Создать статический метод для подсчета гласных.
# ==============================================================


class TextUtils:
    @staticmethod
    def count_vowels(text):
        vowels = "аеёиоуыэюя"
        return sum(1 for symbol in text if symbol in vowels)


print()
print(TextUtils.count_vowels("программирование"))


# ==============================================================
# Задание 29.6
# Создать статический метод для проверки пароля.
# Пароль подходит, если его длина не меньше 8.
# ==============================================================


class Validator:
    @staticmethod
    def is_password_valid(password):
        return len(password) >= 8


print()
print(Validator.is_password_valid("qwerty"))


# ==============================================================
# Задание 29.7
# Создать статический метод для вычисления площади прямоугольника.
# ==============================================================


class Geometry:
    @staticmethod
    def rectangle_area(width, height):
        return width * height


print()
print(Geometry.rectangle_area(4, 5))


# ==============================================================
# Задание 29.8
# Создать статический метод для перевода градусов Цельсия в Фаренгейты.
# ==============================================================


class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32


print()
print(Temperature.celsius_to_fahrenheit(20))


# ==============================================================
# Задание 29.9
# Создать статический метод для удаления пробелов в начале и конце строки.
# ==============================================================


class Cleaner:
    @staticmethod
    def strip_text(text):
        return text.strip()


print()
print(Cleaner.strip_text("  hello  "))


# ==============================================================
# Задание 29.10
# Создать статический метод для проверки, является ли строка палиндромом.
# ==============================================================


class Palindrome:
    @staticmethod
    def is_palindrome(text):
        prepared = text.lower().replace(" ", "")
        return prepared == prepared[::-1]


print()
print(Palindrome.is_palindrome("А роза упала на лапу Азора"))
