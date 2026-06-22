#Splitting Things into Groups

total_students=int(input("Enter the total students in the class:"))
team_size=int(input("Enter the required team size:"))
full_teams=total_students//team_size
leftover=total_students%team_size
print(f'We can form {full_teams} full teams, with {leftover} students left over')
