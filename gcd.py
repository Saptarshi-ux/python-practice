# This code will help to find the greatest common divisor of two numbers from user

a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
while b!=0:
  a,b=b,a%b
print(f"the Greatest Common Divisor is {a}")

# Explanation:
"""The while b != 0: loop repeatedly updates the values of a and b using a % b (remainder operation). In each iteration:
b becomes the new value of a
a % b becomes the new value of b
This process continues until b becomes 0. 
At that point, the remaining value in a is the Greatest Common Divisor (GCD).
This method is called the Euclidean Algorithm, which is an efficient way to compute the GCD of two numbers. """
