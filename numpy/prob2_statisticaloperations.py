import numpy as n
marks=n.array([40,45,88,60,79,60, 75, 85, 73, 90, 55, 80])
print(f'Our data is: {marks}')

#Finding the mean of marks:
mean=round(n.mean(marks),0)
print(f'\n The Average Marks of the class is: {mean}')

#Finding the Median of the marks:
median=n.median(marks)
print(f'\n The Median marks of the class: {median}')

#Scatterness of the data:
sd=n.std(marks)
var=n.var(marks)
print(f'''\n---- The measures of scatterness -----
the standard deviation is: {sd}
the Variance is: {var}''')

#Maximum and minimum values:
max=n.max(marks)
min=n.min(marks)
range=max-min
print(f'''\n---- The maximum and minimum values are: -----
the highest marks obtained is: {max}
the lowest marks obtained is: {min}
the spread of the marking distribution is: {range}''')

#Total Marks:
total=n.sum(marks)
print(f'\n The Total Marks is: {total}')

#Percentile: The value below which 75% of the data lies
per75=round(n.percentile(marks,75),0)
print(f'\n The value below which 75% of the data lies is: {per75}')

#Standard Error of Mean:

sem=round(n.std(marks)/n.sqrt(len(marks)),0)
print("\n ---- The Standard Error of Mean of the Marks is ----")
print("Stadard Error:", sem)

