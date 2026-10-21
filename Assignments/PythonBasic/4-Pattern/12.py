# a => 97

# a
# ab
# abc
# abcd
# abcde

for i in range(1,6):
    alphabet = 97
    for j in range(1,i+1):
        print(chr(alphabet), end="")
        alphabet+=1
    print()