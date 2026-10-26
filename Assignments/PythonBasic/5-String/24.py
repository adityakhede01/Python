# 24. Reverse every word without changing the word order.
# Example: "Python is easy" → "nohtyP si ysae"

s = "Python is easy"
l = s.split() # ['Python', 'is', 'easy']

for i in range(len(l)):
    sub_s = list(l[i]) # ['P','y','t','h','o','n'], ['i','s'], ['e','a','s','y']
    for j in range(len(sub_s)//2):
        sub_s[j],sub_s[len(sub_s)-j-1] = sub_s[len(sub_s)-j-1],sub_s[j]
    string = ''.join(sub_s)
    print(string,end=' ')