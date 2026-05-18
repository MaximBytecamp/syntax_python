# ==============================================================
# Задание 6.13
# Пользователь вводит числа, пока не введёт 0.
# Найти среднее арифметическое положительных чисел.
# ==============================================================

total_positive = 0
count_positive = 0

number = int(input("Введите число: "))
while number != 0:
    if number > 0:
        total_positive += number
        count_positive += 1

    number = int(input("Введите число: "))

if count_positive > 0:
    mean = total_positive / count_positive
    print(f"Среднее положительных чисел = {mean}")
else:
    print("Положительных чисел не было")
