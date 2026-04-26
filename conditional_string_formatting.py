# Problem (detailed):
""" The task is to iterate through a list of car names and apply different formatting rules depending on a condition. If a car name contains the letter 'a', 
It should be converted to uppercase; otherwise, it should be converted to title case. This helps understand how to combine loops, 
conditions, and string methods for dynamic output."""

cars=['bmv','audi','kia']
for i in cars:
  if 'a' in i:
    print(i.upper(),end=' ')
  else:
    print(i.title(),end=' ')

# Code & Output Explanation:
# The list cars = ['bmv','audi','kia'] is iterated one by one. For each string, the condition if 'a' in i checks whether it contains the letter 'a'.

#'bmv' → does not contain 'a', so title() is applied → Bmv
#'audi' → contains 'a', so upper() is applied → AUDI
#'kia' → contains 'a', so upper() is applied → KIA

# All outputs are printed continuously using end=' ' that is with space, resulting in: Bmv AUDI KIA
