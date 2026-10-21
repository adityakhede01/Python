# A => 65

# A
# AB
# ABC
# ABCD
# ABCDE

for i in range(1,6):
    alphabet = 65
    for j in range(1,i+1):
        print(chr(alphabet), end="")
        alphabet+=1
    print()