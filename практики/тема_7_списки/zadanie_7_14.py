from random import randint


# ==============================================================
# Задание 7.14
# Создать список из 10 случайных чисел.
# Сформировать новый список только из положительных чётных чисел.
# ==============================================================

numbers = []
result = []

for _ in range(10):
    numbers.append(randint(-30, 30))

for number in numbers:
    if number > 0 and number % 2 == 0:
        result.append(number)

print(f"Исходный список: {numbers}")
print(f"Положительные чётные числа: {result}")
