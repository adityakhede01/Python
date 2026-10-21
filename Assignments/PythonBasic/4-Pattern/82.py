#    *
#   *_* 
#  *___* 
# *_____*
#  *___* 
#   *_*
#    *

n=7
break_point=n//2+1

for i in range(1,n+1):
    if i<=break_point:
        for _ in range(break_point-i):
            print(" ",end="")
        for j in range(1,2*i):
            if j==1 or j==2*i-1:
                print("*",end="")
            else:
                print("_",end="")
    else:
        for _ in range(i-break_point):
            print(" ",end="")
        j-=2
        k=1
        while k<=j:
            if k==1 or k==j:
                print("*",end="")
            else:
                print("_",end="")
            k+=1
    print()