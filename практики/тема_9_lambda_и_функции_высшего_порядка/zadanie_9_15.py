# ==============================================================
# Задание 9.15
# Дан список строк. Оставить только строки, которые начинаются
# с заданной буквы, и отсортировать их по длине.
# ==============================================================

words = ["python", "java", "pascal", "php", "javascript", "perl"]
letter = input("Введите первую букву: ").lower()

filtered_words = list(filter(lambda word: word.startswith(letter), words))
filtered_words.sort(key=lambda word: len(word))

print(filtered_words)
