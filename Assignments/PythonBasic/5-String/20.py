# 20. Remove duplicate characters while preserving their original order.
# Example: "programming" → "progamin"

s="programming"
seen=set() # Checking it already exist or not => only for optimization
res=[] # Storing the string in list for fast operation (elsewhere new string object will be created every time)

for ch in s:
    if ch not in seen:
        seen.add(ch)
        res.append(ch)
print(''.join(res))