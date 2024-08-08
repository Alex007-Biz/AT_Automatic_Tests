import pytest
from main_HW import count_vowels

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("world") == 1
    assert count_vowels("Python") == 1
    assert count_vowels("AEIOU") == 5
    assert count_vowels("bcdfgh") == 0
    assert count_vowels("") == 0
    assert count_vowels("This is a test string.") == 5
    assert count_vowels("1234567890") == 0
    assert count_vowels("A quick brown fox jumps over the lazy dog") == 11

if __name__ == "__main__":
    pytest.main()