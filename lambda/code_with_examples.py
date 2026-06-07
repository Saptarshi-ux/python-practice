#finding the cuberoot of any number:

cube_r=lambda x: x**(1/3)
n=int(input("enter a number:"))
print(f'The cube root of {n} is {cube_r(n)}')

#detecting even and odd
is_even=lambda x: x%2==0
n=int(input("enter a number:"))
print(f'The number {n} is Even:- {is_even(n)}')

#check whether the number is positive or negative

check_n=lambda x: 'Positive Number' if x>0 else ('It is Zero' if x == 0 else 'Negative Number')
n = float(input("enter a number: "))
print(f'the number {n} is {check_n(n)}')
