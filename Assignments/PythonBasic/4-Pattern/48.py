#     A
#    AB
#   A_C
#  A__D
# ABCDE

n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        if i==n:
            print(chr(64+k),end="")
        else:
            if k==1 or k==i:
                print(chr(64+k),end="")
            else:
                print("_",end="")
    print()