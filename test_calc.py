import pytest

from utils.calc import my_sum, my_avg


def test_empty():
    assert my_sum([]) == 0


def test_one_element():
    assert my_sum([1]) == 1
    assert my_sum([2]) == 2


def test_multiple_elements():
    assert my_sum([1, 2]) == 3
    assert my_sum([1, 2, 3]) == 6


def test_average_empty():
    with pytest.raises(ValueError):
        my_avg([])


def test_average():
    assert my_avg([1]) == 1
    assert my_avg([1, 2, 3]) == 2
    assert my_avg([1, 2]) == 1.5
