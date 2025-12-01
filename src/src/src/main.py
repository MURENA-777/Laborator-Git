#!/usr/bin/env python3
"""
Основной модуль программы.
Демонстрация использования Git и GitHub.
"""

def main():
    """Главная функция программы."""
    print("=== Лабораторная работа №10 ===")
    print("Управление проектом на GitHub")
    print("Hello from Git!")
    
    # Демонстрация изменений из шага 3
    print("This line was added in commit 2")
    
    # Результат работы
    result = calculate_sum(10, 20)
    print(f"Sum: {result}")

def calculate_sum(a, b):
    """Вычисляет сумму двух чисел."""
    return a + b

if __name__ == "__main__":
    main()
