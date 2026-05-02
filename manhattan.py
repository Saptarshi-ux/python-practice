#Manhattan Distance
x1=float(input("enter the value of x1:"))
y1=float(input("enter the value of y1:"))
x2=float(input("enter the value of x2:"))
y2=float(input("enter the value of y2:"))

dis=round(abs((x2-x1))+abs(y2-y1),0)
print(f"the Manhattan distance between ({x1},{y1})"
      f" and ({x2},{y2}) is:  {dis}")


""" In Machine Learning, Manhattan Distance is primarily used as a distance metric in algorithms
like K-Nearest Neighbors (KNN) and K-Means clustering, especially when dealing with high-dimensional 
data where it often outperforms Euclidean distance. Because it calculates the sum of
absolute differences rather than squared ones, it is significantly more robust to outliers, 
preventing extreme values from disproportionately skewing results. It is the preferred choice 
for datasets with discrete or binary attributes and is essential in L1 regularization (Lasso) 
  to encourage feature sparsity by penalizing the absolute magnitude of coefficients."""
