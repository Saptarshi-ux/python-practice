# Walrus Operator (:=)
"""The walrus operator allows you to assign a value to a variable 
while simultaneously using it in an expression. In simple terms, it lets you combine assignment and condition checking in one line."""

# An Example:
while (data:=input("enter a text:"))!= "exit":
  print("Make America Great Again!")

# explanation:
"""The line while (data := input("enter a text:")) != "exit": does two things at once:

Takes user input and assigns it to the variable data
Checks if the entered value is not "exit"

As long as the user does not type "exit", the loop continues and prints "Make America Great Again!". 
The moment the user enters "exit", the condition becomes false, and the loop stops."""
