# 16) …... -9 -6 -3	0 3	6 9	……. n terms [where n is even]

n=int(input("Enter a number: "))

for i in range(n-1,0,-1):
    print(f"-{i*3}",end=" ")
for i in range(n):
    print(i*3,end=" ")