# A
# BCD
# EFGHI
# JKLMNOP

alphabet=65
n=4
for i in range(n):
    for j in range(2*i+1):
        print(chr(alphabet),end="")
        alphabet+=1
    print()