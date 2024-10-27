import pytest


def palindrome(string):
    if type(string) != str:
        raise TypeError()

    string_len = len(string)
    if string_len < 3:
        raise ValueError('Вы ввели строку < 3 символов!')

    for i in range(len(string)):
        if string[i] != string[string_len - i - 1]:
            return False

    return True
    # return string == string[::-1]


def test_palindrome_true():
    assert palindrome('derevered') is True


def test_palindrome_false():
    assert palindrome('derevo') is False


def test_type_exception_palindrome_int():
    with pytest.raises(TypeError):
        palindrome(123)


def test_type_exception_palindrome_list():
    with pytest.raises(TypeError):
        palindrome(['abba', '1221', 'azxza'])  # Итерируемый тип данных


def test_type_exception_palindrome_none():
    with pytest.raises(TypeError):
        palindrome(None)


def test_value_exception_palindrome_len():
    with pytest.raises(ValueError):
        palindrome('vb')
