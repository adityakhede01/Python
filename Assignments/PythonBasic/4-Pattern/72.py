# A B C D E
#  A B C D
#   A B C
#    A B
#     A

n=5
for i in range(1,n+1):
    for _ in range(1,i):
        print(" ",end="")
    for j in range(1,n-i+2):
        print(f"{chr(64+j)} ",end="")
    print()