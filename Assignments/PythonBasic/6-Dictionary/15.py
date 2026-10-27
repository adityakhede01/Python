# 15. Create a dictionary in which numbers from 1 to 5 are keys and their squares are values.

d={}
for key in range(1,6):
    d[key]=key*key
print(d)