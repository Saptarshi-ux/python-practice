""" Suppose you are given a list, from which you have been asked to extract the both 
index and values together without using loop."""
#THE CODE:
l=[33,45,12,99,0,4,5,3,88,47,56,61]
for index, value in enumerate(l):
  print(f"the value {value} correspnds to {index} index position")

# Explanation:
"""The enumerate() function in Python is used to iterate over a sequence while automatically
keeping track of the index of each element. Instead of manually creating and updating a counter variable, 
enumerate() pairs each item in the iterable with its corresponding position and returns them as 
tuples of (index, value). This makes the code cleaner and more readable, 
especially when you need both the element and its index at the same time.
It is commonly used in loops to simplify tasks that involve tracking positions within a list, tuple, or any iterable."""
