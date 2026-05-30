#Extract user name from an email id

email=input('ENTER YOUR EMAIL ID: (ALL IN LOWER CASE)')
un=''
for i in email:
  if i=='@':
    break
  un+=i
print(f'Your email id is: {email}\nAnd Your Username is:{un}')

# Explanation:
"""if i == '@': break: This is the lookout. Before doing anything else, 
it checks if the current letter is the @ symbol. If it is, the break command triggers. 
break instantly kills the loop and stops checking any more letters.
un += i: If the letter wasn't the @ symbol, the program skips the break and comes to this line.
This takes the current letter (i) and glues it to the end of our un text box."""

