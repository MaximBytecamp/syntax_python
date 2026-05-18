# ==============================================================
# Задание 11.15
# Даны ответы двух учеников на тест.
# Найти номера вопросов, на которые оба ответили правильно,
# и номера вопросов, где правильный ответ был только у первого.
# ==============================================================

first_student_correct = {1, 2, 4, 7, 9}
second_student_correct = {2, 3, 4, 8, 9}

both_correct = first_student_correct & second_student_correct
only_first = first_student_correct - second_student_correct

print(f"Оба ответили правильно: {both_correct}")
print(f"Правильно только у первого: {only_first}")
