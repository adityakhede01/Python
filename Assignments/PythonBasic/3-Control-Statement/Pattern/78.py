#    1
#   12
#  123
# 1234
#  123
#   12
#    1

n=7
break_point = n//2+1
ctr_space_after_break=1

for i in range(1,n+1):
    if i<=break_point:
        for _ in range(1,break_point-i+1):
            print(" ",end="")
        for j in range(1,i+1):
            print(j,end="")
    else:
        for _ in range(1,ctr_space_after_break+1):
            print(" ",end="")
        ctr_space_after_break+=1
        for k in range(1,(n-i+1)+1):
            print(k,end="")
    print()