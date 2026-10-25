# 123456789
#  1234567
#   12345
#    123
#     1

n=5
for i in range(1,n+1):
    for _ in range(1,i):
        print(" ",end="")
    for j in range(1,(2*n-2*i+1)+1):
        print(j,end="")
    print()