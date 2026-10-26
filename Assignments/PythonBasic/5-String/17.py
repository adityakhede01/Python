# 17. Find the first non-repeating character in a string.
# Example: "aabbcddee" → c

a='aabbcddee'
freq={}
for ch in a:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

for key,value in freq.items():
    if value==1:
        print(f"First non-repeating character: {key}")
        break