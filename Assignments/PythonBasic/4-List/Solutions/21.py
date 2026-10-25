# Max Sum in configuration
# Given an array(0-based indexing), you have to find the max sum of i*A[i] where A[i] is the element at index i in the array.The only operation allowed is to rotate(clock-wise or counter clock-wise) the array any number of times.

a=[8,3,1,2]
max=float('-inf')
for c in range(len(a)):
    stored=a[0]
    sum=0
    for i in range(len(a)-1):
        a[i]=a[i+1]
    a[-1]=stored
    for i in range(len(a)):
        sum+=i*a[i]
    if sum>max: max=sum
print(max)