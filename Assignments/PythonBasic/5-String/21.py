# 21. Find the most frequent character in a string.

s="findfrequentcharacter"
freq={}
max=float('-inf')

for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

for value in freq.values():
    if value>max:
        max=value
for key in freq.keys():
    if freq[key]==max:
        print(key,end=" ")