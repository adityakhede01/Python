# 30. Suppose A, B, C are arrays of integers of size M, N, and M + N respectively. The numbers in array A appear in ascending order while the numbers in array B appear in descending order. Write a java progtam to produce third array C by merging arrays A and B in ascending order. . 

# a = [10,20,30,40,50,60]
# b = [100,90,80,70]
a = [10,20,35,40]
b = [35,30,20]
c=[]

c1=0
c2=len(b)-1

while c1<len(a) and c2>=0 :
    if a[c1] <= b[c2]:
        c.append(a[c1])
        c1+=1
    else:
        c.append(b[c2])
        c2-=1

while c1<len(a):
    c.append(a[c1])
    c1+=1
while c2>=0:
    c.append(b[c2])
    c2-=1

print(c)