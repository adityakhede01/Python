# 11. Create a dictionary from two lists: one list contains keys and the other contains values. Do not use zip().

keys=['a','b','c']
values=[1,2,3]
d={}
for i in range(len(keys)):
    d[keys[i]] = values[i]
print(d)