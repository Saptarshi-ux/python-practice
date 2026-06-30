#Example with 3D array

import numpy as n
arr=n.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[0,1,0]+arr[1,0,2])

#Explanation:
"""This code creates a 3D NumPy array of two stacked 2x3 grids and uses [block, row, column] indexing to 
extract specific values.
It retrieves the number 4 from the first block's second row (arr[0,1,0]) and 
the number 9 from the second block's first row (arr[1,0,2]).
Finally, it adds these two values together, printing the ultimate result of 13"""
