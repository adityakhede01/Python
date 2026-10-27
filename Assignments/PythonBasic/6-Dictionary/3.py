# 3. Check whether the key "age" exists in a dictionary.

student = {
   'name':'Aditya',
   'age': 19,
   'marks': 10
}

for detail in student:
    if detail == 'age':
        print("Key age exists")
        break
else:
    print("Key age doesn't exist")