# Given an unsorted array arr[] of size N having both negative and positive integers. The task is place all negative element at the end of array without changing the order of positive element and negative element.

arr = [1, -1, 3, 2, -7, -5, 11, 6]
pos = []
neg = []

for i in range(len(arr)):
    if arr[i]<0:
        neg.append(arr[i])
    else:
        pos.append(arr[i])

result = pos+neg
print(result)