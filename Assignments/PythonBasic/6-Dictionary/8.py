# 8. Calculate the sum of all numeric values in a dictionary.

student = {
   'name':'Aditya',
   'age': 19,
   'marks': 10
}
total=0
for i in student:
    if type(student[i]) in (int,float):
        total+=student[i]
print(total)