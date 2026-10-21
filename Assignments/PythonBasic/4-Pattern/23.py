# a
# bc
# d f
# g  j
# klmno

alphabet=97
for i in range(1,6):
    for j in range(1,i+1):
        if j==1 or i==5 or i==j:
            print(chr(alphabet),end="")
        else:
            print(" ",end="")
        alphabet+=1
    print()