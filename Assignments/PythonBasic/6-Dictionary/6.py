# 6. Remove a key from a dictionary using pop(). Handle the case where the key does not exist.

student = {
   'name':'Aditya',
   'age': 19,
   'marks': 10
}

student.pop('wrongKey',None)
print(student)