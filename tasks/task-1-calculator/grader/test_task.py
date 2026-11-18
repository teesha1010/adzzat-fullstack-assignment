
import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1])
)

from app import add, subtract, multiply, divide

def test_addition():
    assert add(5, 3) == 8

def test_subtraction():
    assert subtract(5, 3) == 2

def test_multiplication():
    assert multiply(5, 3) == 15

def test_normal_division():
    assert divide(10, 2) == 5

def test_decimal_division():
    assert divide(5, 2) == 2.5

def test_division_by_zero():
    try:
        divide(10, 0)
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        pass