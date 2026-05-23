#Remove duplicates from list

list1=[int(a) for a in input("Enter numbers separated by single space:").split()]
unique_list=list(set(list1))
print(f'The original list is:\n {list1}\n The final list after removing the duplicates is:\n {unique_list}')
