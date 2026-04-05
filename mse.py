""" create a function that calculates the mean squared error by averaging the squares of 
the differences between corresponding elements of two equal-length arrays."""
def solution(array_a, array_b):
    squared_diffs = [(a - b)**2 for a, b in zip(array_a, array_b)]
    return sum(squared_diffs) / len(array_a)
