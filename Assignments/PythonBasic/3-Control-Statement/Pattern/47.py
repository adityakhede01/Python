#     1
#    11
#   1*1
#  1**1
# 11111

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==5 or j==5 or i+j==6:
            print("1",end="")
        elif i+j>6:
            print("*",end="")
        else:
            print(" ",end="")
    print()