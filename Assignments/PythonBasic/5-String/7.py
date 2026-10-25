# 7. Convert lowercase characters to uppercase without using upper().
#   s = "inDor434e"  => "INDOR434E"

s = "inDor434e"
l=list(s)
for i in range(len(l)):
    if 'a'<=l[i]<='z':
        l[i] = chr(ord(l[i])-32)
a="".join(l)
print(a)

'''
s = "inDor434e"
result=''.join(
    chr(ord(ch)-32) if 'a'<=ch<='z' else ch for ch in s
)
print(result)
'''