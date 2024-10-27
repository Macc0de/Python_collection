# pytest -v main.py через терминал
import pytest


def factorial(num):
    if type(num) != int:
        raise TypeError()

    if num < 0:
        raise ValueError('Вы ввели число < 0!')
    elif num == 0:
        return 1

    res = num
    while num > 1:
        res *= (num - 1)
        num -= 1

    return res


def test_factorial_null():
    assert factorial(0) == 1


def test_factorial_three():
    assert factorial(3) == 6


def test_type_exception_factorial_str():
    with pytest.raises(TypeError):
        factorial('text')  # Итерируемый тип данных


def test_type_exception_factorial_float():
    with pytest.raises(TypeError):
        factorial(1.23)


def test_type_exception_factorial_none():
    with pytest.raises(TypeError):
        factorial(None)


def test_value_exception_factorial():
    with pytest.raises(ValueError):
        factorial(-4)
