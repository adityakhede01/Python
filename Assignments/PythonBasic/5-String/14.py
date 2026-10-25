# 14. Remove all digits from a string.

s="aditya12isgreat34!"
l=list(s)
for i in range(len(l)):
    if '0'<=l[i]<='9':
        l[i]=''
s=''.join(l)
print(s)