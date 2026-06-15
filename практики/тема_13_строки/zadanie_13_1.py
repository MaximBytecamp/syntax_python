# ==============================================================
# Задание 13.1
# Пользователь вводит строку.
# Посчитать количество букв, цифр и пробелов.
# ==============================================================

text = input("Введите строку: ")
letters = 0
digits = 0
spaces = 0

for symbol in text:
    if symbol.isalpha():
        letters += 1
    elif symbol.isdigit():
        digits += 1
    elif symbol == " ":
        spaces += 1

print("Букв:", letters)
print("Цифр:", digits)
print("Пробелов:", spaces)
