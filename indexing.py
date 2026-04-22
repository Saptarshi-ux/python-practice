x=[10,(20,30),40]
y=x[1][0]
print(y-x[0])


# the output is 10

""" This problem is about understanding nested data structures and indexing in Python, 
specifically how to access elements inside a tuple that is stored within a list, 
and then perform a simple arithmetic operation on the extracted values."""

# Explaination:
""" In the code, x = [10, (20,30), 40] creates a list where the second element is a tuple. 
To get the required value, y = x[1][0] is used: x[1] accesses the tuple (20,30), and [0] 
then extracts its first element, which is 20. After that, print(y - x[0]) 
subtracts the first element of the list (10) from y (20). Since 20 - 10 = 10, the output is 10."""
