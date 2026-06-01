#finding the largest element in a list by using the for loop, not the sort method

x=[int(a) for a in input("Enter numbers separated by single space:").split()]
largest=x[0]
for i in x:
  if i>largest:
    largest=i
print(f'The largest element from the list {x} is 👉 {largest}')

#But in the above problem, I have found a bug which is not very serious, but it hinders the code from being perfect.
#So I have modified that part. In the first code, if by chance the user passes an empty list, then it will throw an INDEX ERROR. So to meet this gap,
#I have modified the code in this way:

x=[int(a) for a in input("Enter numbers separated by single space:").split()]
if x==[]:
  print("The list is empty")
elif x!=[]:
  largest=x[0]
  for i in x:
    if i>largest:
      largest=i
  print(f'The largest element from the list {x} is 👉 {largest}')

#Now solving the same problem using .sort() method
