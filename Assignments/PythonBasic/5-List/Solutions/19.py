# Find Maximum product contigeous sub array 
# Given an array Arr[] that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray.

a=[6, -3, -10, 0, 2]
# a=[2, 3, 4, 5, -1, 0]

index=0
max=float('-inf')
product=1
while index<len(a):
    product*=a[index]
    if product>max:max=product
    index+=1
print(max)