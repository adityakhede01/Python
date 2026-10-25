# 8. Remove all spaces from a string.

s = "remove my spaces"
l=list(s)
for i in range(len(l)):
    if l[i]==' ': l[i]=''
a=''.join(l)
print(a)