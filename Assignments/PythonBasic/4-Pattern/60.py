#     X 
#    XX 
#   X__X
#  X____X
# X X X X X

n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    if i!=n :
        for k in range(i):
            if k==0:
                print("X",end="")
            elif k==i-1:
                print("X",end="")
            else:
                print("__",end="")
    else:
        for l in range(n):
            print("X ",end="")
    print()