#finding the cuberoot of any number:

cube_r=lambda x: x**(1/3)
n=int(input("enter a number:"))
print(f'The cube root of {n} is {cube_r(n)}')

#detecting even and odd
is_even=lambda x: x%2==0
n=int(input("enter a number:"))
print(f'The number {n} is Even:- {is_even(n)}')
