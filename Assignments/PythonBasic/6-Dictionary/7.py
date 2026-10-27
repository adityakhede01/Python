# 7. Find the number of key-value pairs in a dictionary without using len().

count=0
student = {
   'name':'Aditya',
   'age': 19,
   'marks': 10
}

for detail in student:
   count+=1
print(f"Length of dict: {count}")