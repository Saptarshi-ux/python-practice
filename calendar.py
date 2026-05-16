#Write a Program to display calendar

import calendar as c
year=int(input("enter the year:"))
month_name=input("Enter the first three letter of the month required (eg. 'Jan'):").strip().title()
month_number = list(c.month_abbr).index(month_name)
cal=c.month(year, month_number)
print(cal)
