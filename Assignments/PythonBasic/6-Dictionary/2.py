# 2. Given a dictionary of student details, print each key and value on a separate line.

student = {
   'name':'Aditya',
   'age': 19,
   'marks': 10
}

for detail in student:
   print(f"Key: {detail} & Value: {student[detail]}")