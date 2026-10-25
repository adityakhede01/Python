# 10. Replace every space with a hyphen (-).

s="aditya is here"
l=list(s)
for i in range(len(l)):
    if l[i]==" ": l[i]='-'
s=''.join(l)
print(s)

'''
# Or
print(s.replce(" ", "-"))
'''