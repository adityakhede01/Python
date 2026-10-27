# 9. Find the key associated with the largest value in a dictionary.

student = {
   'a': 20,
   'b': 10,
   'c':30
}
largest=float('-inf')

for i in student:
    if student[i]>largest:
        largest=student[i]
        key=i
print(key)