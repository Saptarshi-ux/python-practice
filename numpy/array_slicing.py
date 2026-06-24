import numpy as n
arr=n.array([1,2,3,4,5,6])
x=arr.reshape(2,3)
y=x[:,1:]+x[:,:-1]
print(n.sum(y[0]*y[1]))

#Explanation:
""" This NumPy code first takes a sequence of numbers from 1 to 6 and reshapes it into a 2x3 matrix where the top row is [1, 2, 3] 
and the bottom row is [4, 5, 6]. It then performs two column slices on this matrix creating one sub matrix 
by dropping the first column and another by dropping the last column, and adds them together element-by-element 
generate a new matrix `y` containing the values [[3, 5], [9, 11]]. Finally, the code extracts the first row of this new matrix ([3, 5]), 
multiplies it element-by-element with the second row ([9, 11]) to produce the array [27, 55], 
and calculates the sum of those two numbers to print the final result of 82."""
