#Remove and Pop

n=[10,20,30,30]
print(f'The original list is: {n}')
x=n.remove(30)
print(f'the removed value is {x}')
print(f'the list after removing the value is {n}')

y=n.pop(2)
print(f'the removed item is: {y}')

#The Difference Between remove() and pop()
# What they target (Value vs. Index):

""".remove(value) deletes based on the actual item. In our code, 
n.remove(30) tells Python to search the list and delete the first occurrence of the number 30, 
regardless of where it is located."""

""".pop(index) deletes based on the position. In our code, 
n.pop(2) tells Python to go straight to index position 2 and delete whatever happens to be sitting there. 
(If we leave the brackets empty like .pop(), it automatically deletes the very last item)."""

#What they return:

""".remove() returns None. It does the job silently without giving us anything back 
to save in a variable (which is why your x becomes None)."""

""".pop() returns the deleted item. It pulls the value out of the list and hands 
it back to us so we can store it or use it (which is why it successfully stores the number 30)."""
