import pytest


def count_more_one(string):
    if type(string) != str:
        raise TypeError()

    count = 0
    for i in "".join(set(string)):  # set уникальные символы
        if string.count(i) > 1:
            count += 1

    return count


def test_count_more_one_unique():
    assert count_more_one('max') == 0


def test_count_more_one_repeat():
    assert count_more_one('maximumx') == 2


def test_type_exception_count_more_one_int():
    with pytest.raises(TypeError):
        count_more_one(123)


def test_type_exception_count_more_one_list():
    with pytest.raises(TypeError):
        count_more_one(['gbbg', '8768', 'xxxx'])


def test_type_exception_count_more_one_none():
    with pytest.raises(TypeError):
        count_more_one(None)
