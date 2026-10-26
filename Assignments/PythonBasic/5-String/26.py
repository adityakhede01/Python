# 26. Find the longest word in a sentence.

s="I am going to do homework now"
l = s.split()
max_len=float('-inf')
max_index=None

for i in range(len(l)):
    if len(l[i])>max_len:
        max_len=len(l[i])
        max_index=i
print(l[max_index])