# 21. Combine two dictionaries by adding the values of common keys.
#     Example: {'a': 10, 'b': 20} and {'b': 5, 'c': 7}
#     Expected: {'a': 10, 'b': 25, 'c': 7}

d1 = {'a': 10, 'b': 20}
d2 = {'b': 5, 'c': 7}
for el in d2:
    if el in d1:
        d1[el] += d2[el]
    else:
        d1[el] = d2[el]
print(d1)