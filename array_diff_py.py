def array_diff(a, b):
    b = set(b)
    return [x for x in a if x not in b]

