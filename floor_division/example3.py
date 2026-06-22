#Chop off the last digit


score=int(input("enter a number in three digit"))
first_dig=score//100
second_dig=(score//10)%10
third_dig=score%10
print("\n---- After Digit Separation ----")
print("The first digit from the left is", first_dig)
print("The second digit from the left is", second_dig)
print("The third digit from the left is", third_dig)
