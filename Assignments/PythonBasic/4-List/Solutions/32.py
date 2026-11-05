# 32. Given two arrays of integers A and B of sizes M and N respectively. Write a Write a java program, which will produce a third array named C. such that the following sequence is followed. 
# All even numbers of A from left to right are copied into C from left to right. 
# All odd numbers of A from left to right are copied into C from right to left. 
# All even numbers of B from left to right are copied into C from left to right. 
# All odd numbers of B from left to right are copied into C from right to left.
# e.g., A is {3, 2, 1, 7, 6, 3} and B is {9, 3, 5, 6, 2, 8, 10} the resultant array C is {2, 6, 6, 2, 8, 10, 5, 3, 9, 3, 7, 1, 3}

a = [3, 2, 1, 7, 6, 3]
b = [9, 3, 5, 6, 2, 8, 10]
c = []

for i in range(len(a)):
    if a[i] % 2 == 0:
        c.append(a[i])
for i in range(len(b)):
    if b[i] % 2 == 0:
        c.append(b[i])
for i in range(len(b)-1,-1,-1):
    if b[i] % 2 !=0:
        c.append(b[i])
for i in range(len(a)-1,-1,-1):
    if a[i] % 2 !=0:
        c.append(a[i])

print(c)