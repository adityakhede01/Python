# 55555
#  4__4
#   3_3
#    22
#     1

n=5
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,(n-i+1)+1):
        if i==1:
            print(n-i+1,end="")
        else:
            if k==1 or k==(n-i+1) :
                print(n-i+1,end="")
            else:
                print("_",end="")
    print()