import pytest
from main4 import sort_list

def test_sort():
    assert sort_list([5, 6, 3, 1, 2]) == [1, 2, 3, 5, 6]

def test_sort():
    assert sort_list([-1, 3, 0, -2, 2]) == [-2, -1, 0, 2, 3]