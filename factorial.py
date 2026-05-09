#Factorial using recursion

def fact(x):
  if x<0:
    return "you have entered a negative number"
  elif x<=1:
    return 1 
  else:
    return x*fact(x-1)

#Output:
#fact(5):-> 120, which is nothing but 5!
#fact (0):-> 1, zero factorial is one
#fact(-2):-> 'you have entered a negative number'
