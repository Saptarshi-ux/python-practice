import numpy as n
ar=n.array([5,10,15])
x=ar//5
print(x.sum())

#Explanation:
"""The // symbol is Python's "floor division" (or integer division) operator. Because you are using NumPy, 
it takes that rule and instantly applies it to every single number in the array at the same time (a concept called "broadcasting").
5 // 5 = 1
10 // 5 = 2
15 // 5 = 3
x becomes the new array: [1, 2, 3]"""
