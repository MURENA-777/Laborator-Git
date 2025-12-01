"""
Модуль с дополнительным функционалом.
Создан в ветке feature/new-functionality.
"""

def new_feature():
    """Демонстрационная функция из новой ветки."""
    return "This is a new feature!"

def multiply(x, y):
    """Умножает два числа."""
    return x * y

if __name__ == "__main__":
    print("Feature module loaded")
    print(f"2 * 3 = {multiply(2, 3)}")
