# 1. Write a program to reverse a string without using slicing ([::-1]).

'''
    # Time complexity: O(n^2) => Python lists are immutable, every time in char+rev python creates new string and copies the existing characters.
s='aditya'
rev=''
for char in s:
    rev = char+rev
print(rev)
'''

# Time complexity: O(n)
s='aditya'
l=list(s)
# print(l) => ['a', 'd', 'i', 't', 'y', 'a']
for i in range(len(l)//2):
    l[i],l[len(l)-i-1] = l[len(l)-i-1],l[i]
a="".join(l)
print(a)