# A
# AB
# A C
# A  D
# ABCDE

for i in range(1,6):
    alphabet=65
    for j in range(1,6):
        if j==1 or i==5 or i==j:
            print(chr(alphabet),end="")
        else:
            print(" ",end="")
        alphabet+=1
    print()