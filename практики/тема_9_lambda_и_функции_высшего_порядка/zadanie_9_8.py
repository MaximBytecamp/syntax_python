# ==============================================================
# Задание 9.8
# Написать функцию, которая принимает другую функцию и число.
# ==============================================================

def apply_to_number(number, operation):
    return operation(number)

print(apply_to_number(5, lambda x: x ** 2))
print(apply_to_number(5, lambda x: x + 100))
