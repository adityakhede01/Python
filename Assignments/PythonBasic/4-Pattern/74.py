# 123456789
#  1     7
#   1   5
#    1 3
#     1

n=5
for i in range(1,n+1):
    for _ in range(1,i):
        print(" ",end="")
    for j in range(1,(2*n-2*i+1)+1):
        if i!=1:
            if j==1 or j==2*n-2*i+1 :
                print(j,end="")
            else:
                print(" ",end="")
        else:
            print(j,end="")
    print()