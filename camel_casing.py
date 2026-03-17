# create a function that breaks up camel casing, using a space between words

def solution(s):
    result = ""
    for i in s:
        if i.isupper():
            result += " "
        result += i
    return result
