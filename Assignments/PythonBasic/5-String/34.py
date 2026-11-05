# 34. Compress a string by counting consecutive repeated characters.
# Example: "aaabbccccd" → "a3b2c4d1"

s="aaabbccccd"
count={}
for ch in s:
    count[ch] = count.get(ch, 0) + 1
for i in count:
    print(f"{i}{count[i]}",end="")


'''
s = "aaabbccccd"

result = []
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result.append(s[i-1] + str(count))
        count = 1

result.append(s[-1] + str(count))

print("".join(result))
'''