# Q.14. Find the first non-repeating elment in given array of integers
# Find the first non-repeating element in a given array arr of N integers.
# Note: Array consists of only positive and negative integers and not zero.

a=[-1, 2, -1, 3, 2]
# a=[1, 1, 1]

for i in range(len(a)):
    flag=True
    for j in range(len(a)):
        if a[i]==a[j] and j!=i:
            flag=False
            break
    if flag:
        print(a[i])
        break
else:
    print(0)