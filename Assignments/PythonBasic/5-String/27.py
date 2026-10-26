# 27. Find all duplicate characters and their frequencies.

s="aditya is going on mars"
freq={}

for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

for key in freq:
    if freq[key]>1:
        print(f"Character: {key} & frequency: {freq[key]}")
