#How to find Least Common Multiple (LCM)

x=abs(int(input("Enter a number:")))
y=abs(int(input("Enter another number:")))
larger=max(x,y)
while True:
  if larger%x==0 and larger%y==0:
    print(f'the LCM of {x} and {y} is: {larger}')
    break
  larger+=1
