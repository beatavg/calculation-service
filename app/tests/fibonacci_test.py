from app.services.fibonacci import fibonacci
import pytest

# Valid input
def test_fibonacci_0():
    assert fibonacci(0) == 0

def test_fibonacci_1():
    assert fibonacci(1) == 1

def test_fibonacci_5():
    assert fibonacci(5) == 5

def test_fibonacci_10():
    assert fibonacci(10) == 55

# Invalid input
def test_fibonacci_negative_number():
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_fibonacci_string():
    with pytest.raises(TypeError):
        fibonacci("hello")

def test_fibonacci_float():
    with pytest.raises(TypeError):
        fibonacci(3.14)

def test_fibonacci_none():
    with pytest.raises(TypeError):
        fibonacci(None)