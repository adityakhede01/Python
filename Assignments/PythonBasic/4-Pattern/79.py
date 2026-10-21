# 1
# 1 2
# 1  3
# 1   4
# 1  3
# 1 2
# 1

n=7
for i in range(1,n+1):
    if i<=n//2+1:
        for j in range(1,i+1):
            if j==1 or j==i:
                print(j,end="")
            else:
                print(" ",end="")
    else:
        for k in range(1,(n-i+1)+1):
            if k==1 or k==n-i+1:
                print(k,end="")
            else:
                print(" ",end="")
    print()