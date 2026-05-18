# ==============================================================
# Задание 7.15
# Дан список оценок. Найти:
# а) средний балл;
# б) количество двоек;
# в) лучшую оценку;
# г) отсортированный список оценок.
# ==============================================================

marks = [5, 4, 3, 5, 2, 4, 5, 3, 2]

mean = sum(marks) / len(marks)
count_twos = marks.count(2)
best_mark = max(marks)

sorted_marks = marks.copy()
sorted_marks.sort(reverse=True)

print(f"Оценки: {marks}")
print(f"Средний балл = {mean:.2f}")
print(f"Количество двоек = {count_twos}")
print(f"Лучшая оценка = {best_mark}")
print(f"Оценки по убыванию: {sorted_marks}")
