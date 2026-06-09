#Finding the factorial of a number using conditional expessions:

n=int(input("Enter a number: "))
factorial=1
if n<0:
  print(f'You have entered {n} which is a negative number. Factorial doesnt exists for negative number')
elif n<=1:
  print(f' Factrial of {n} is 1')
else:
  for i in range(2,n+1):
    factorial=factorial*i
  print(f'Factorial of {n} is {factorial}')
