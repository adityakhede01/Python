# 18. Find the first repeating character.
# Example: "programming" → r

s="programming"
freq={}
for ch in s:
    if ch in freq:
        print(ch)
        break
    else:
        freq[ch]=0
else:
    print("No repeating character")