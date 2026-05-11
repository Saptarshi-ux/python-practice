# Odd and Even number detection from user-given input
a=int(input("Enter a number:"))
if a%2:
  print(f"The number {a} is odd")
else:
  print(f"The number {a} is even")
  
#Explanation:
""" This code takes an integer input from the user and uses the modulo operator (%) to calculate the remainder 
when the number is divided by 2. Because Python evaluates a remainder of 1 as True and 0 as False, 
the if statement elegantly triggers the "odd" block for remainders of 1, and the else block for a remainder of 0."""
