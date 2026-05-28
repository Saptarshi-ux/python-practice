#Extract user name from an email id

email=input('ENTER YOUR EMAIL ID: (ALL IN LOWER CASE)')
un=''
for i in email:
  if i=='@':
    break
  un+=i
print(f'Your email id is: {email}\nAnd Your Username is:{un}')

# Explanation:
