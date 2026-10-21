# a
# bc
# def
# ghij
# klmno

alphabet=97
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(alphabet), end="")
        alphabet+=1
    print()