#Problem on Array Method in Numpy
import numpy as n
arr=n.array([2,4,6,8])
x=n.insert(arr,2,10)
y=n.delete(x,1)
print(y.max()-y.min()+len(x))
