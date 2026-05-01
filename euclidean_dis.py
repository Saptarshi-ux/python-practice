"""Problem (detailed):
The task is to find the shortest distance between two points in a 2D plane given their coordinates (x1,y1) and
(x2​,y2). This is based on the distance formula from geometry, which uses the differences in x and y coordinates to compute the straight-line (Euclidean) distance."""

#Code:
import math
x1=float(input("enter the value of x1:"))
y1=float(input("enter the value of y1:"))
x2=float(input("enter the value of x2:"))
y2=float(input("enter the value of y2:"))

dis=round(math.sqrt((x2-x1)**2+(y2-y1)**2),0)
print(f"the shortest distance between ({x1},{y1})"         #Multiple f-strings to write the long print statement in two segments
      f" and ({x2},{y2}) is:  {dis}")
