# 26. Write a program to find the largest and smallest element of an array.

l=[1,2,34,567,32,43]
smallest=float('+inf')
largest=float('-inf')
for i in range(len(l)):
    if l[i]>largest: largest=l[i]
    if l[i]<smallest: smallest=l[i]
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")