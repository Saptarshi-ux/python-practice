a=[1,5,7]
b=a
a=a+[4]
x=[i for i in a if i not in b ]
print(b)
print(a)
print(x)

# Explanation:
"""The code begins by creating a list [1, 5, 7] and assigning it to a, and then b = a makes b point to 
that exact same list in memory. The "trick" of the problem happens at a = a + [4]; 
instead of modifying the original list, the + operator forces Python to create a completely new list [1, 5, 7, 4] 
and assigns it to a, leaving b untouched and still pointing to the original [1, 5, 7]. 
Next, a list comprehension iterates through the new list a and filters out any elements that also exist in b, 
successfully isolating the newly added number. As a result, 
the code prints the original untouched list b ([1, 5, 7]), 
the newly created list a ([1, 5, 7, 4]), and the extracted difference x ([4])"""
