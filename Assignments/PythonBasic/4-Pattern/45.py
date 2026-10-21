#     5
#    44
#   333
#  2222
# 11111

n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print(n-i+1,end="")
    print()