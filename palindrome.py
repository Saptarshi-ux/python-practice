""" Check if a number is Palindrome or not without slicing A palindrome number 
is a kind of number which remains the same when its digits are reversed, 
reading the same forwards and backwards. Examples include 121, 33, 505, 404 and 12321. 
They are effectively "mirror images" of themselves, with the 
first half of the number corresponding to the second half in reverse order."""

num=int(input("enter a number:"))
a=num
rev=0
while num>0:
  digit=num%10
  rev=rev*10+digit
  num=num//10
if a==rev:
  print(f" the number {a} is a Palindrome type")
else:
  print(f" the number {a} is not a Palindrome type")
