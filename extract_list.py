""" Problem (detailed):
The goal is to access the first and last elements of a list without using traditional methods like loops or indexing (l[0], l[-1]). 
Instead, it uses Python’s unpacking feature, which allows splitting a list into variables in a clean and readable way. T
his approach is useful for writing more elegant and Pythonic code."""


l=[1,2,3,4,5,5,6,7,8,9,0]
first, *all, last=l
print(f"the first element is {first}")
print(f"the last element is {last}")
print(f"the all other elements are {all}")

# Code (line-by-line explanation):
"""
l = [1,2,3,4,5,5,6,7,8,9,0] → Creates the list
first, *all, last = l →
first gets the first element → 1
last gets the last element → 0
*all collects all remaining middle elements into a list
print(f"the first element is {first}") → prints first element
print(f"the last element is {last}") → prints last element
print(f"the all other elements are {all}") → prints middle elements
"""
