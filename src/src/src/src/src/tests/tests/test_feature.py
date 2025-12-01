"""
Тесты для нового функционала.
"""

from src.feature import multiply, new_feature

def test_multiply():
    """Тест функции умножения."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    print("✓ Тесты умножения пройдены")

def test_new_feature():
    """Тест новой функции."""
    result = new_feature()
    assert "feature" in result.lower()
    print("✓ Тест новой функции пройден")

if __name__ == "__main__":
    test_multiply()
    test_new_feature()
