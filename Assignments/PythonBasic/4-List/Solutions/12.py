# Find common elements in three sorted arrays.
# Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
# Note: can you take care of the duplicates without using any additional Data Structure?

a1=[1, 5, 10, 20, 40, 80]
a2=[6, 7, 20, 80, 100]
a3=[3, 4, 15, 20, 30, 70, 80, 120]
res=[]
i=0; j=0; k=0

while i<len(a1) and j<len(a2) and k<len(a3):
    if a1[i]==a2[j]==a3[k]:
        if not res or res[-1]!=a1[i]:
            res.append(a1[i])
        i+=1; j+=1; k+=1
    elif a1[i]<a2[j]:
        i+=1
    elif a2[j]<a3[k]:
        j+=1
    else:
        k+=1
print(res)