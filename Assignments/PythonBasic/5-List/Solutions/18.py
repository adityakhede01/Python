# Find largest sum contigeous sub array
# Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

# float('-inf') --> Minimum number in python

a=[1,2,3,-2,5]
# a=[-1,-2,-3,-4]

# max=float('-inf')
# for i in range(len(a)):
#     sum=0
#     for j in range(i,len(a)):
#         sum+=a[j]
#         if sum>max: max=sum
# print(max)

index=0
max=float('-inf')
sum=0
while index<len(a):
    sum+=a[index]
    if sum>max:max=sum
    index+=1
print(max)