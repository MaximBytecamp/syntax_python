# ==============================================================
# Задание 5.14
# Дана строка. Посчитать количество гласных, согласных и цифр.
# Пробелы и знаки препинания не учитывать.
# ==============================================================

text = input("Введите строку: ").lower()

vowels = "аеёиоуыэюяaeiou"
count_vowels = 0
count_consonants = 0
count_digits = 0

for symbol in text:
    if symbol.isdigit():
        count_digits += 1
    elif symbol.isalpha():
        if symbol in vowels:
            count_vowels += 1
        else:
            count_consonants += 1

print(f"Гласных: {count_vowels}")
print(f"Согласных: {count_consonants}")
print(f"Цифр: {count_digits}")
