# 11111
#  2222
#   333
#    44
#     5

n=5
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,(n-i+1)+1):
        print(i,end="")
    print()