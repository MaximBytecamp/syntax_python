# ==============================================================
# Задание 9.9
# Написать функцию apply_operation(a, b, operation).
# ==============================================================

def apply_operation(a, b, operation):
    return operation(a, b)

print(apply_operation(10, 5, lambda a, b: a + b))
print(apply_operation(10, 5, lambda a, b: a * b))
