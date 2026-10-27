# 30. Find the longest common prefix among a list of strings.
# Example: ["flower", "flow", "flight"] → "fl"

l = ["flower", "flow", "flight"]
s=''
prefix=''
for i in range(len(l[0])):
    ch=l[0][i]
    s+=ch

    result = True
    for string in l:
        if s not in string:
            result = False
            break

    if result: # True
        prefix=s
    else:
        break
print(prefix)