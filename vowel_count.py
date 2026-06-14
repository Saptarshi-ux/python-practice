# Count the Vowels in a string

text=input("Enter a text:")
count=0
for ch in text.lower():
  if ch in 'aeiou':
    count+=1
print(f'--- Number of vowels in the text {text} is ---: \n {count} ')
