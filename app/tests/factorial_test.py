from app.services.factorial import factorial
import pytest

# Valid input
def test_factorial_0():
    assert factorial(0) == 1

def test_factorial_1():
    assert factorial(1) == 1

def test_factorial_5():
    assert factorial(5) == 120

def test_factorial_10():
    assert factorial(10) == 3628800

def test_factorial_20():
    assert factorial(20) == 2432902008176640000 # Large number

# Invalid input
def test_factorial_negative_number():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_string():
    with pytest.raises(TypeError):
        factorial("hello")

def test_factorial_float():
    with pytest.raises(TypeError):
        factorial(3.14)

def test_factorial_none():
    with pytest.raises(TypeError):
        factorial(None)