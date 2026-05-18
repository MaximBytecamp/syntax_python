# ==============================================================
# Задание 10.13
# Дан список паролей. Проверить, есть ли хотя бы один надёжный пароль.
# Надёжный пароль: длина не меньше 8, есть цифра и есть заглавная буква.
# ==============================================================

passwords = ["qwerty", "Python2026", "hello123", "CODE"]

has_strong_password = any(
    len(password) >= 8
    and any(symbol.isdigit() for symbol in password)
    and any(symbol.isupper() for symbol in password)
    for password in passwords
)

print(f"Есть надёжный пароль: {has_strong_password}")
