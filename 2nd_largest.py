# Find the second largest element in the list without using sort
list1=[int(a) for a in input("Enter numbers separated by single space:").split()]
largest=list1[0]
largest_2nd=float('-inf')
for i in list1:
  if i>largest:
    largest_2nd=largest
    largest=i
  elif i>largest_2nd and i!=largest:
    largest_2nd=i
print(f'the second largest from the above list is {largest_2nd}')

#Code Explanation:
"""
The code begins by converting the user's space-separated input into a list of integers, 
then initializes the `largest` variable to the first item and `largest_2nd` to negative infinity 
so any real number can safely overwrite it. As it loops through each number in the list, it checks 
if the current number is bigger than the `largest`; 
if so, it demotes the old largest value to `largest_2nd` and crowns the current number as the new `largest`. 
If the current number isn't the absolute biggest but is still larger than the current 
`largest_2nd` (and isn't just a duplicate of the largest), it updates `largest_2nd` to this new number. 
Once the loop finishes evaluating every item, 
it simply prints the final value that was saved in the `largest_2nd` variable."""
