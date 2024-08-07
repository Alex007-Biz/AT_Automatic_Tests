import pytest
from main3 import isPalindrome

def test_is_palindrom_true():
    assert isPalindrome('madam') == True

def test_is_palindrom_false():
    assert isPalindrome('hello') == False

@pytest.mark.parametrize('test_input, expected', [
    ('level', True),
    ('python', False),
    ('racecar', True),
    ('', True),
])

def test_is_palindrom(test_input, expected):
    assert isPalindrome(test_input) == expected

