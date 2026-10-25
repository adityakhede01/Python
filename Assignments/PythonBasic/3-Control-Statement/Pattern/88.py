#     1
#     2
#     3
#     4
# 123454321
#     4
#     3
#     2
#     1

n=9
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==5 and j<=5:
            print(j,end="")
        elif i==5 and j>5:
            print(n-j+1,end="")
        elif j==5 and i<5:
            print(i,end="")
        elif j==5 and i>5:
            print(n-i+1,end="")
        else:
            print(" ",end="")
    print()