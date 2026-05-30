#finding the largest element in a list by using the for loop, not the sort method

x=[int(a) for a in input("Enter numbers separated by single space:").split()]
largest=x[0]
for i in x:
  if i>largest:
    largest=i
print(f'The largest element from the list {x} is 👉 {largest}')
