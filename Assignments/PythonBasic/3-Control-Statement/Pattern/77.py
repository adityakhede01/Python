# 1
# 12
# 123
# 1234
# 123
# 12
# 1

n=7
for i in range(1,n+1):
    if i<=n//2+1:
        for j in range(1,i+1):
            print(j,end="")
    else:
        for k in range(1,(n-i+1)+1):
            print(k,end="")
    print()