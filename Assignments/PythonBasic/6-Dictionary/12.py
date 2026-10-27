# 12. Print all keys, all values, and all key-value pairs of a dictionary.

d={'a':1,'b':2,'c':3}

for key in d.keys():
    print(key,end=" ")
print()
for value in d.values():
    print(value,end=" ")
print()
for key,value in d.items():
    print(f"{key}-{value}", end=" ")