# Problem:
""" The goal is to understand how Python handles list assignments and copies. 
When you assign one list to another variable, both variables point to the same object in memory. However, when you create a copy using slicing ([:]), 
a new independent list is created. The problem then applies different modifications to these lists and checks how those changes impact each list when calculating their sums."""
# The code: 
a=[1,2,3]
b=a
c=a[:]
a.append(4)
b[0]=10
c[1]=20
print(sum(a),sum(b),sum(c))

# Code (line-by-line explanation):

# a = [1,2,3] -> Creates a list a
# b = a -> b points to the same list as a (no new list created)
# c = a[:] -> Creates a new copy of a (different object)
# a.append(4) -> Adds 4 to a -> now a = [1,2,3,4]
# Since b points to the same list, b also becomes [1,2,3,4]
# b[0] = 10 -> Modifies first element -> a = [10,2,3,4] and b = [10,2,3,4]
# (a and b both change because they are the same object)
# c[1] = 20 -> Only changes c -> c = [1,20,3]
# (c is independent, so a and b are unaffected)
# print(sum(a), sum(b), sum(c)) -> Calculates sums:
# sum(a) = 10 + 2 + 3 + 4 = 19
# sum(b) = 19 (same as a)
# sum(c) = 1 + 20 + 3 = 24
