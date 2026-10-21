# Multi line string object
'''
Sub array with given sum
Array of size N containing only non-negative integers, find a continuous sub-array which adds to a given number S

Ex:
Input:
    N=5, S=12
    A=[1,2,3,7,5]
Output:
    2 4
Explanation: The sum of elements from 2nd to 4th position is 12(S).
'''
# Sliding Windows

arr=[1,2,3,7,5]
target=12; N=5 # Size of array
sum=0; left=0; right=0

while left<=right:
    sum+=arr[right]
    if sum==target:
        print(f"{left} {right}")
        break
    while sum>target and left<right:
        sum-=arr[left]
        left+=1
    if sum==target:
        print(f"{left} {right}")
        break
    right+=1