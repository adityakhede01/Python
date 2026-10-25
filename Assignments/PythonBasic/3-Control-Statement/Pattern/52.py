# 12345
#  1__4
#   1_3
#    12
#     1

n=5
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,(n-i+1)+1):
        if i==1:
            print(k,end="")
        else:
            if k==1 or k==(n-i+1) :
                print(k,end="")
            else:
                print("_",end="")
    print()