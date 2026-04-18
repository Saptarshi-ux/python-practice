a=[1,2,3,4]
b=[1,2,3,4]


print(a==b) # Checks value equality (contents of lists)
print (a is b) # this checks whether the identity whether both refer to the same object in memory

"""
Two lists `a = [1,2,3,4]` and `b = [1,2,3,4]` are created with the same values but as separate objects in memory. 
The expression `a == b` checks value equality, meaning it compares the contents of both lists, so it returns 
`True` because all elements are the same. On the other hand, `a is b` checks identity, meaning whether both variables point
to the exact same object in memory, which they do not, so it returns `False`. In simple terms, `==` asks “Are the values the same?” 
while `is` asks “Are they the exact same object?”."""
