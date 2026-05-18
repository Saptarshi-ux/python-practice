#Problem 1: 

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

#Problem 2: 
a=[1,2]
b=[a]
a+=[3]
print(b[0] is a, b)

#Explanation:

"""When we write a += [3], Python does not create a brand new list in memory; 
instead, it acts just like the .extend() method and modifies the original list in-place. 
Because b was created to hold a direct sticky note to a (making b look like [[1, 2]]),
any in-place changes to a will instantly show up inside b. 
Therefore, when the print statement checks if the first item in b is the exact same object as a in memory (b[0] is a),
it correctly evaluates to True, and prints the updated contents showing that b is now [[1, 2, 3]]."""



#Problem 3:
data=(12,18,24)
a,*b=data
for i in range(len(b)):
  b[i]+=a
  a+=4
print(a)
print(b)


#Explanation: 
"""
The code starts with data=(12,18,24), which creates a standard tuple of three numbers. 
Next, a,*b=data uses a Python trick called "extended unpacking,"
where a grabs the first number (12), and the asterisk on *b scoops up all the remaining numbers 
and packs them into a mutable list ([18, 24]). 
  The loop for i in range(len(b)): is set up to run exactly twice because there are two items in list b 
(representing indexes 0 and 1). 
During the first loop cycle (i=0), b[i]+=a adds the current value of a (12) to the first list item (18),
turning it into 30, and a+=4 bumps a up to 16. During the second loop cycle (i=1), 
b[i]+=a adds the newly updated a (16) to the second list item (24), turning it into 40, 
and a+=4 bumps a up again to 20. Finally, print(a) outputs the final updated integer 20, 
and print(b) outputs the modified list [30, 40]"""
