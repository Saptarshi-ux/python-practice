# Implementation of Fizzbuzz:

for i in range(1,101):
  if i%3==0 and i%5==0:
    print("FizzBuzz")
  elif i%3==0:
    print("Fizz")
  elif i%5==0:
    print("Buzz")
  else:
    print(i)

#explanation:
"""In a nutshell: This code loops through the numbers 1 to 100, 
replacing multiples of 3 with Fizz, multiples of 5 with Buzz, and numbers divisible by both with FizzBuzz.

The crucial logic concept here is the order of operations. 
You must check the strictest condition (`i%3==0 and i%5==0`) first. 
If you checked for just 3 first, a number like 15 would trigger "Fizz" 
and the program would skip the rest of the block, completely missing the fact that it was supposed to be a FizzBuzz"""
