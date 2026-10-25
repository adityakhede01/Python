#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

n=5
power=0
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    print(11**power)
    power+=1