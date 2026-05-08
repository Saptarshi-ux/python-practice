def f(n):
  if n<2:
    return n
  return f(n-1)+f(n-2)

print(f(7)) #this will give us the value of 8th number of the Fibo series
