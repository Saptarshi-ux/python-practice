#Example with 3D array

import numpy as n
arr=n.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[0,1,0]+arr[1,0,2])

#explanation:
"""Here arr[block number, row number, col number]"""
