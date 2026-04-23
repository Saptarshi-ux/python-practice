n=[10,20,30]
for i in range(len(n)):
  print(n[-i],end="")

# The Output is: 103020
"""
This problem is about understanding negative indexing and loop behavior in Python, 
specifically how list elements are accessed using negative indices and how that affects the output order."""

# Explaination:
"""
In the code, n = [10, 20, 30] defines a list. The loop runs with i values 0, 1, 2 using range(len(n)). Inside the loop, n[-i] is used:
When i = 0, n[-0] is the same as n[0] → 10
When i = 1, n[-1] → last element → 30
When i = 2, n[-2] → second last element → 20
These values are printed continuously (end=""), so the output becomes 103020
"""
