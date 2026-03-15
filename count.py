# Count characters in a string and return in dict format
from collections import Counter
def count(s):
    return dict(Counter(s))
