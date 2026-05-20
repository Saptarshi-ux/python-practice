# implemented the Triangle Inequality Theorem to check whether three random lengths create a triangle or not

x1=float(input("enter the length of a side of a triangle:"))
x2=float(input("enter the length of another side of a triangle:"))
x3=float(input("enter the length of last side of a triangle:"))

#to check whether x1,x2 and x3 are forming any triangle or not (SSS rule)

if (x1>0 and x2>0 and x3>0) and (x1+x2>x3 and x1+x3>x2 and x2+x3>x1):
  print(f'The result is:\nHere {x1},{x2} and {x3} are forming a triangle')
else:
  print(f'The result is:\nHere {x1}, {x2} and {x3} are not forming a triangle')

#Solving the same problem using a recursion function:

def check_triangle(x1, x2, x3):
    if (x1 > 0 and x2 > 0 and x3 > 0) and (x1 + x2 > x3 and x1 + x3 > x2 and x2 + x3 > x1):
        print(f'The result is:\nHere {x1}, {x2} and {x3} are forming a triangle')
    else:
        print(f'The result is:\nHere {x1}, {x2} and {x3} are not forming a triangle')

x1 = float(input("Enter the length of a side of a triangle: "))
x2 = float(input("Enter the length of another side of a triangle: "))
x3 = float(input("Enter the length of the last side of a triangle: "))

check_triangle(x1, x2, x3)
