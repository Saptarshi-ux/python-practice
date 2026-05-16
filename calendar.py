#Write a Program to display calendar

import calendar as c
year=int(input("enter the year:"))
month_name=input("Enter the first three letter of the month required (eg. 'Jan'):").strip().title()
month_number = list(c.month_abbr).index(month_name)
cal=c.month(year, month_number)
print(cal)The calendar module has a hidden list of abbreviations that looks like this: ['', 'Jan', 'Feb', 'Mar', ...]


#Code Explanation:
#part 1: strip().title()
"""This is a safety measure. It removes accidental spaces and ensures the text always starts with 
a capital letter followed by lowercase (so if you type "jan", "JAN", or " Jan ", it perfectly formats it to "Jan")"""

#Part 2:c.month_abbr
# The calendar module has a hidden list of abbreviations that looks like this: ['', 'Jan', 'Feb', 'Mar', ......]

#Part 3:.index()
"""By converting that abbreviation list into a standard Python list, 
we can use the .index() method to ask Python, "What position is 'Jan' in?" 
Python will see it is at position 1 and automatically assign 1 to month_number,
allowing the rest of your original code to work perfectly"""


