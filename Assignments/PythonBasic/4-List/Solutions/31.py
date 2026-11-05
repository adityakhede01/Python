# 31. Suppose X. Y, Z are arrays of integers of size M, N, and M + N respectively. The numbers in array X and Y appear in descending order. Write a java program to produce third array Z by merging arrays X and Y in descending order. 

x = [50,40,30,20,10]
y = [45,35,25,15]
z = []

c1=0
c2=0

while c1<len(x) and c2<len(y):
    if x[c1] >= y[c2]:
        z.append(x[c1])
        c1+=1
    else:
        z.append(y[c2])
        c2+=1

while c1<len(x):
    z.append(x[c1])
    c1+=1
while c2<len(y):
    z.append(y[c2])
    c2+=1

print(z)