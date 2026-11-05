# 24. Group a list of words according to their length.
#     Example: ["cat", "apple", "dog", "mango"]
#     Expected groups: 3 -> ["cat", "dog"], 5 -> ["apple", "mango"]

l = ["cat", "apple", "dog", "mango"]
freq={}
for el in l:
    length = len(el)
    if length in freq:
        freq[length].append(el)
    else:
        freq[length]=[]
        freq[length].append(el)
print(freq)