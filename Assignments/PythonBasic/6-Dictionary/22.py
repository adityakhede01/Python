# 22. Find the common keys between two dictionaries.

d1 = {'a': 10, 'b': 20, 'd':30}
d2 = {'b': 5, 'c': 7, 'd':40}
for el in d2:
    if el in d1:
        print(el,end=" ")