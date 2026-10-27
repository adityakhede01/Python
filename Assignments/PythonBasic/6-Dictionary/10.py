# 10. Merge two dictionaries. If a key exists in both dictionaries, use the value from the second dictionary.


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
for key in dict2:
    dict1[key] = dict2[key]
print(dict1)

'''
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)
'''