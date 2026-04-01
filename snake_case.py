""" Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. 
Lowercase characters can be numbers. If the method gets a number as input, it should return a string"""
def to_underscore(string):
    if not isinstance(string, str):
        return str(string)
    r = ""
    for i, char in enumerate(string):
        if char.isupper() and i > 0:
            r += "_"
        r += char.lower()
    return r
