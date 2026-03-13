"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit."""

def persistence(num):
    count = 0
    while num >= 10:
        i = 1
        for dig in str(num):
            i *= int(dig)
        num = i
        count += 1  
    return count
