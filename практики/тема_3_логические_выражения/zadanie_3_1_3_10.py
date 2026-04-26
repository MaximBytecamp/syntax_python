# ==============================================================
# Задания 3.1, 3.3, 3.5, 3.7, 3.10
# Вычисление значений логических выражений
# ==============================================================

# Исходные значения (для большинства заданий):
# А = Истина (True), В = Ложь (False), С = Ложь (False)

# Приоритет операторов (ключевая идея темы):
# not > and > or 

A = True
B = False
C = False

print("=" * 50)
print(f"A = {A}, B = {B}, C = {C}")
print("=" * 50)


# ==============================================================
# Задание 3.1
# Вычислить значения логических выражений при А=True, В=False, С=False
# ==============================================================

print("\n--- Задание 3.1 ---")

# а) А или В
# A = True, B = False
# True или False = True  (достаточно одного True)
result_a = A or B
print(f"а) A or B  →  True or False  =  {result_a}")

# б) А и В
# A = True, B = False
# True и False = False  (нужны оба True)
result_b = A and B
print(f"б) A and B  →  True and False  =  {result_b}")

# в) В или С
# B = False, C = False
# False или False = False  (оба False — результат False)
result_c = B or C
print(f"в) B or C  →  False or False  =  {result_c}")


# ==============================================================
# Задание 3.3
# Вычислить значения логических выражений при А=True, В=False, С=False
# ==============================================================

print("\n--- Задание 3.3 ---")

# а) не А и В
# not A = not True = False
# False и B = False and False = False
result_a = not A and B
print(f"а) not A and B  →  not True and False  →  False and False  =  {result_a}")

# б) А или не В
# not B = not False = True
# A или True = True or True = True
result_b = A or not B
print(f"б) A or not B  →  True or not False  →  True or True  =  {result_b}")

# в) А и В или С
# Приоритет: «и» выполняется раньше «или»
# Шаг 1: A and B = True and False = False
# Шаг 2: False or C = False or False = False
result_c = A and B or C
print(f"в) A and B or C  →  (True and False) or False  →  False or False  =  {result_c}")


# ==============================================================
# Задание 3.5
# Вычислить значения логических выражений при А=True, В=False, С=False
# ==============================================================

print("\n--- Задание 3.5 ---")

# а) А или В и не С
# Приоритет: not > and > or
# Шаг 1: not C = not False = True
# Шаг 2: B and True = False and True = False
# Шаг 3: A or False = True or False = True
result_a = A or B and not C
print(f"а) A or B and not C  →  True or (False and not False)  →  True or (False and True)  →  True or False  =  {result_a}")

# б) не А и не В
# Шаг 1: not A = not True = False
# Шаг 2: not B = not False = True
# Шаг 3: False and True = False
result_b = not A and not B
print(f"б) not A and not B  →  not True and not False  →  False and True  =  {result_b}")

# в) не (А и С) или В
# Шаг 1: A and C = True and False = False
# Шаг 2: not False = True
# Шаг 3: True or B = True or False = True
result_c = not (A and C) or B
print(f"в) not (A and C) or B  →  not (True and False) or False  →  not False or False  →  True or False  =  {result_c}")

# г) А и не В или С
# Шаг 1: not B = not False = True
# Шаг 2: A and True = True and True = True
# Шаг 3: True or C = True or False = True
result_g = A and not B or C
print(f"г) A and not B or C  →  (True and not False) or False  →  (True and True) or False  →  True or False  =  {result_g}")

# д) А и (не В или С)
# Шаг 1: not B = not False = True
# Шаг 2: True or C = True or False = True  (скобки выполняются первыми)
# Шаг 3: A and True = True and True = True
result_d = A and (not B or C)
print(f"д) A and (not B or C)  →  True and (not False or False)  →  True and (True or False)  →  True and True  =  {result_d}")

# е) А или (не (В и С))
# Шаг 1: B and C = False and False = False
# Шаг 2: not False = True
# Шаг 3: A or True = True or True = True
result_e = A or (not (B and C))
print(f"е) A or not (B and C)  →  True or not (False and False)  →  True or not False  →  True or True  =  {result_e}")


# ==============================================================
# Задание 3.7
# Вычислить значения логических выражений при А=True, В=False, С=False
# ==============================================================

print("\n--- Задание 3.7 ---")

# а) А или не (А и В) или С
# Шаг 1: A and B = True and False = False
# Шаг 2: not False = True
# Шаг 3: A or True = True or True = True
# Шаг 4: True or C = True or False = True
result_a = A or not (A and B) or C
print(f"а) A or not(A and B) or C  →  True or not(True and False) or False  →  True or not False or False  →  True or True or False  =  {result_a}")

# б) не А или А и (В или С)
# Шаг 1: not A = not True = False
# Шаг 2: B or C = False or False = False  (скобки)
# Шаг 3: A and False = True and False = False  (and раньше or)
# Шаг 4: False or False = False
result_b = not A or A and (B or C)
print(f"б) not A or A and (B or C)  →  not True or True and (False or False)  →  False or True and False  →  False or False  =  {result_b}")

# в) (А или В и не С) и С
# Шаг 1: not C = not False = True
# Шаг 2: B and True = False and True = False  (and раньше or внутри скобок)
# Шаг 3: A or False = True or False = True  (скобки)
# Шаг 4: True and C = True and False = False
result_c = (A or B and not C) and C
print(f"в) (A or B and not C) and C  →  (True or False and True) and False  →  (True or False) and False  →  True and False  =  {result_c}")


# ==============================================================
# Задание 3.10
# Вычислить значения логических выражений при А=False, В=False, С=True
# ==============================================================

print("\n--- Задание 3.10 ---")

# Меняем значения переменных!
A = False
B = False
C = True

print(f"A = {A}, B = {B}, C = {C}")

# а) (не А или не В) и не С
# Шаг 1: not A = not False = True
# Шаг 2: not B = not False = True
# Шаг 3: True or True = True  (скобки)
# Шаг 4: not C = not True = False
# Шаг 5: True and False = False
result_a = (not A or not B) and not C
print(f"а) (not A or not B) and not C  →  (True or True) and not True  →  True and False  =  {result_a}")

# б) (не А или не В) и (А или В)
# Шаг 1: not A = True, not B = True
# Шаг 2: True or True = True  (левые скобки)
# Шаг 3: A or B = False or False = False  (правые скобки)
# Шаг 4: True and False = False
result_b = (not A or not B) and (A or B)
print(f"б) (not A or not B) and (A or B)  →  (True or True) and (False or False)  →  True and False  =  {result_b}")

# в) А и В или А и С или не С
# Приоритет: not > and > or, выполняем слева направо группы «and»
# Шаг 1: A and B = False and False = False
# Шаг 2: A and C = False and True = False
# Шаг 3: not C = not True = False
# Шаг 4: False or False or False = False
result_c = A and B or A and C or not C
print(f"в) A and B or A and C or not C  →  (False and False) or (False and True) or not True  →  False or False or False  =  {result_c}")
