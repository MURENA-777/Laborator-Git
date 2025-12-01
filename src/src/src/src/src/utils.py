"""
Вспомогательные утилиты.
"""

def greet_user(name):
    """Приветствует пользователя."""
    return f"Hello, {name}!"

def validate_email(email):
    """Проверяет email на валидность."""
    return "@" in email and "." in email
