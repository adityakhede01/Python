# 20. Reverse a dictionary so that values become keys and keys become values. Assume all values are unique.

dictionary={'a':1,'b':2,'c':3}
new_dict={}
for el in dictionary:
    new_dict[dictionary[el]] = el
print(new_dict)