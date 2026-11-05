# 18. Find the first non-repeating character in a string using a dictionary.

s = 'aditya'
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

for key,value in freq.items():
    if value==1:
        print(f"First non-repeating character is {key}")
        break