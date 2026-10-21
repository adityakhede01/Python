# Find it there is any subarray with sum equals to zero
# Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.

a=[5,4,2,-3,1,6]
# a=[5,4,2,0,1,6]

target=0
flag=False
for i in range(len(a)):
    sum=0
    for j in range(i,len(a)):
        sum+=a[j]
        if sum==target:
            flag=True
            break
    if flag:
        print("Yes")
        break
else:
    print("No")


# The Sliding Window technique => for subarray

# target=0
# sum=0; left=0; right=0
# while left<=right:
#     sum+=a[right]
#     if sum==target:
#         print("Yes")
#         break
#     while sum>target and left<right:
#         sum-=a[left]
#         left+=1
#     if sum==target:
#         print("Yes")
#         break
#     right+=1
# else:
#     print("No")