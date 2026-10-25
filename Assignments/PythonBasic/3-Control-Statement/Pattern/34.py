# EEEEE
# DDDD
# CCC
# BB
# A

n=5
alphabet=69
for i in range(n):
    for j in range(n-i):
        print(chr(alphabet),end="")
    alphabet-=1
    print()