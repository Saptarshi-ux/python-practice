#Write a function where it will detect whether it is prime or not
def prime(n):
  if n<2:
    return "it is not a prime"
  for i in range(2,n):
    if n%i==0:
      return "It is not a prime number"
    else:
      return 'It is a prime'
