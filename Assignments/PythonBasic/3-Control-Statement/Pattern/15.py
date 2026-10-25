# A
# BB
# CCC
# DDDD
# EEEEE

alphabet=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(alphabet), end="")
    print()
    alphabet+=1