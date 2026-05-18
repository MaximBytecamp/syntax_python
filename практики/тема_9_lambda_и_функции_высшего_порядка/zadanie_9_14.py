# ==============================================================
# Задание 9.14
# Написать функцию process_numbers(numbers, operation),
# которая применяет operation к каждому числу списка.
# ==============================================================

def process_numbers(numbers, operation):
    result = []

    for number in numbers:
        result.append(operation(number))

    return result


numbers = [1, 2, 3, 4, 5]

print(process_numbers(numbers, lambda x: x ** 2))
print(process_numbers(numbers, lambda x: x * 10))
print(process_numbers(numbers, lambda x: x - 1))
