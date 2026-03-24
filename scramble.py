""" Complete the function scramble(str1, str2) that returns true 
if a portion of str1 characters can be rearranged to match str2, otherwise returns false."""
from collections import Counter
def scramble(str1, str2):
    counts1 = Counter(str1)
    counts2 = Counter(str2)
    for char, count in counts2.items():
        if counts1[char] < count:
            return False
    return True
