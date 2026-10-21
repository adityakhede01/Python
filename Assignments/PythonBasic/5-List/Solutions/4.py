# Sorting of array

arr = [123,6,0,87]

for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j] = arr[j],arr[i]

print(f"Reverse array: {arr}")