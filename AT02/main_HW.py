def count_vowels(s):
    """Функция для подсчета количества гласных в строке."""
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count