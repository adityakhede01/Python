#     *
#    *_*
#   *___* 
#  *_____* 
# *********

row=5
for i in range(1,row+1):
    for j in range(row,i,-1):
        print(" ",end="")
    print("*",end="")
    for k in range(1,(2*i-3)+1):
        if i>1 and i<=row-1:
            print("_",end="")
        if i==row:
            print("*",end="")
    if i!=1: print("*",end="")
    print()