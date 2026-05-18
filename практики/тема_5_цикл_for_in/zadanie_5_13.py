# ==============================================================
# Задание 5.13
# Пользователь вводит n чисел. Найти:
# а) сумму чётных чисел;
# б) количество отрицательных чисел;
# в) максимальное число.
# ==============================================================

n = int(input("Сколько чисел ввести: "))

sum_even = 0
count_negative = 0
max_number = None

for i in range(n):
    number = int(input(f"Введите число {i + 1}: "))

    if number % 2 == 0:
        sum_even += number

    if number < 0:
        count_negative += 1

    if max_number is None or number > max_number:
        max_number = number

print(f"Сумма чётных чисел = {sum_even}")
print(f"Количество отрицательных чисел = {count_negative}")
print(f"Максимальное число = {max_number}")
