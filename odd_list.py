#Extracting odd numbers from a list given by the user

list1=[int(a) for a in input("Enter numbers separated by single space:").split()]
list_odd=[]
for i in list1:
  if i%2!=0:
    list_odd.append(i)
print(f"The list of odd numbers is {list_odd}")
