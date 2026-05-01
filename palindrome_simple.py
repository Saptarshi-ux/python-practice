#The Same Problem now Using the Slicing method
""" The goal is to determine if a given number is a palindrome ot not. 
Instead of using loops or complex logic, 
the number is treated as a string and compared with its reversed version using slicing."""
num=input("enter a number:")
if num ==num[::-1]:
  print(f" the number {num} is a Palindrome type")
else:
  print(f" the number {num} is not a Palindrome type")
