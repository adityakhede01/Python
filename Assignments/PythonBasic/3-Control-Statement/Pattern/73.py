# 5 5 5 5 5
#  4 4 4 4
#   3 3 3
#    2 2
#     1

n=5
for i in range(1,n+1):
    for _ in range(1,i):
        print(" ",end="")
    for j in range(1,n-i+2):
        print(f"{n-i+1} ",end="")
    print()