# 35. Expand a compressed string.
# Example: "a3b2c4" → "aaabbcccc"

s = "a3b2c4"
result = []

for i in range(0, len(s), 2):
    ch = s[i]
    count = int(s[i+1])
    result.append(ch * count)

print("".join(result))