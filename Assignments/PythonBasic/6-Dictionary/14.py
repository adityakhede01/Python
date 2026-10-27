# 14. Copy a dictionary into another dictionary. Explain whether changing a nested object in the copy can affect the original.

'''
Note:
d2 = d1
    Assignment (not a copy). Both variables refer to the same dictionary.
    Both variables point to the same dictionary. Any modification to the dictionary through either variable affects the same object.
d2 = d1.copy()
    Shallow copy--> Creates a new outer dictionary, but nested mutable objects are shared.
    Creates a new outer dictionary, but nested mutable objects, such as lists, are still shared.
d2 = copy.deepcopy(d1)
    Deep copy --> It requires copy.deepcopy(d2) from Python's copy module.
'''

d1 = {'a':1,'b':[10,20],'c':3}

# d2 = d1.copy()
d2 = {}
for key in d1:
    d2[key] = d1[key]

d2['b'].append(30)
d2['a'] = 10

print(f"d1: {d1}")
print(f"d2: {d2}")