#     A
#    A B
#   A B C
#  A B C D
# A B C D E  

n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print(f"{chr(65+k)} ",end="")
    print()