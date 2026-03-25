"""
Write a function that takes a string input and returns the first character that is not repeated anywhere in the string.
For example, if given the input "stress", the function should return 't', since the letter t only occurs once in the string, and occurs first in the string."""
from collections import Counter
def first_non_repeating_letter(s):
    counts = Counter(s.lower())
    for char in s:
        if counts[char.lower()] == 1:
            return char
    return ""
