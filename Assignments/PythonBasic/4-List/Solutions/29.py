# 29. Suppose a one-dimensional array AR containing integers is arranged in ascending order. Write a java program to search for an integer from AR with the help of Binary search method, 

arr=[5,7,9,20,35,48,50]

left=0
right=len(arr)-1
val_search=48
mid=(left+right)//2

while left<right:
    if arr[mid]==val_search:
        print(f"{val_search} found")
        break
    elif arr[mid]<val_search:
        left=mid+1
    elif arr[mid]>val_search:
        right=mid
    mid=(left+right)//2
else:
    print(f"{val_search} not found")