#     1
#    1*1
#   1***1
#  1*****1
# 111111111

n=5
for i in range(1,n+1):
    for _ in range(n-i):
        print(" ",end="")
    for j in range(1,2*i):
        if i!=n and i!=1:
            if j==1 or j==2*i-1 :
                print("1",end="")
            else:
                print("*",end="")
        else:
            print("1",end="")
    print()