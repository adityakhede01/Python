# x
# xx
# xxx
# xxxx
# xxx
# xx
# x

n=7
for i in range(1,n+1):
    if i<=n//2+1:
        for _ in range(1,i+1):
            print("x",end="")
    else:
        for _ in range(1,(n-i+1)+1):
            print("x",end="")
    print()