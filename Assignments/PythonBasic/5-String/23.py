# 23. Reverse the order of words in a sentence.
# Example: "Python is easy" → "easy is Python"

s="Python is easy"
l = s.split()

# Reversing the array
for i in range(len(l)//2):
    l[i],l[len(l)-i-1]=l[len(l)-i-1],l[i]

res = " ".join(l)
print(res)