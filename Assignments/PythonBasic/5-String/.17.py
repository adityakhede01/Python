# 17. Find the first non-repeating character in a string.
# Example: "aabbcddee" → c

a='aabbcddee'
s=set()
for i in range(len(a)-1,-1,-1):
    if a[i] not in s:
        s.add(a[i])
    else:
        s.remove(a[i])
print(s)