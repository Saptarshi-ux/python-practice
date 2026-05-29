# detect Pythagorean triples

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))
numbers = sorted([a, b, c])
if numbers[0]**2 + numbers[1]**2 == numbers[2]**2:
    print(f"{a}, {b}, and {c} are Pythagorean triples")
else:
    print(f"{a}, {b}, and {c} are not Pythagorean triples")
