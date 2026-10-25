# ABCDE
# ABCD
# ABC
# AB
# A

n=5
for i in range(n):
    alphabet=65
    for j in range(n-i):
        print(chr(alphabet),end="")
        alphabet+=1
    print()