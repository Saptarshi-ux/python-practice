"""
Here just like Problem 14: We are here also extract the values and index from a list
But here we try to solve this using simple for loop"""

# THE CODE:
l=[33,45,12,99,0,4,5,3,88,47,56,61]
for value in l:
  index=l.index(value)
  print(f"{value} correspnds to the index position of"
  f" {index} in the given list")
