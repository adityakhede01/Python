#    *
#   ***
#  ***** 
# ******* 
#  ***** 
#   *** 
#    *

n=7
break_point=n//2+1

for i in range(1,n+1):
    if i<=break_point:
        for _ in range(break_point-i):
            print(" ",end="")
        for j in range(1,2*i):
            print("*",end="")
    else:
        for _ in range(i-break_point):
            print(" ",end="")
        j-=2
        k=1
        while k<=j:
            print("*",end="")
            k+=1
    print()