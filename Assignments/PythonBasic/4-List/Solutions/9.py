# Q.9 Find the Union and Intersaction of two sorted array.
# Given two arrays a[] and b[] of size n and m unionpectively. The task is to find union between these two arrays. 
# Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.

# Union
# Taking sorted(in ascending order) array

# To check duplicate: if not union or union[-1]!=a1[i]
# not union orFalse when empty else true, because for empty the -1 index doesn't exist.
# union[-1]!=a1[i]-> If last index matches then doesn't add again.

a1=[1,2,2,3,4,5]; a2=[1,2,3,3]
union=[]; intersection=[]
i=0; j=0

while i<len(a1) and j<len(a2):
    if a1[i]==a2[j]:
        if not union or union[-1]!=a1[i]:
            union.append(a1[i])
            intersection.append(a1[i])
        i+=1; j+=1
    elif a1[i]<a2[j]:
        if not union or union[-1]!=a1[i]:
            union.append(a1[i])
        i+=1
    else:
        if not union or union[-1]!=a2[j]:
            union.append(a2[j])
        j+=1

while i<len(a1):
    if not union or union[-1]!=a1[i]:
        union.append(a1[i])
    i+=1
while j<len(a2):
    if not union or union[-1]!=a2[j]:
        union.append(a2[j])
    j+=1

print(f"union: {union}")
print(f"intersection: {intersection}")