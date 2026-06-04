#Sorting in a dictionary data in ascending order

data=[{"ID": "A01","Name":"Rahul", "Marks": 77},
     {"ID": "A02","Name": "Rita", "Marks": 89},
     {"ID": "A03","Name": "Sam", "Marks": 64},
     {"ID": "A04","Name":"Priya", "Marks": 81}]

from operator import itemgetter
sorted_data=sorted(data, key=itemgetter("Marks"))
for r in sorted_data:
  print(r)

#Here, the sorting is based on the dictionary element "Marks"

#The next part:

#Now sorting in a dictionary data in descending order. The code is:

data=[{"ID": "A01","Name":"Rahul", "Marks": 77},
     {"ID": "A02","Name": "Rita", "Marks": 89},
     {"ID": "A03","Name": "Sam", "Marks": 64},
     {"ID": "A04","Name":"Priya", "Marks": 81}]

from operator import itemgetter
sorted_data=sorted(data, key=itemgetter("Marks"), reverse=True)     #Here just I added reverse criteria
for r in sorted_data:
  print(r)

