"""
Тесты для основного модуля.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.main import calculate_sum

def test_calculate_sum():
    """Тест функции сложения."""
    assert calculate_sum(2, 3) == 5
    assert calculate_sum(-1, 1) == 0
    assert calculate_sum(0, 0) == 0
    print("✓ Все тесты пройдены")

if __name__ == "__main__":
    test_calculate_sum()
