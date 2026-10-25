# kth largest and kth smallest
# For sorted(ascending) data

arr = [1,5,7,8,9]
k = int(input("Kth element: "))

if k <= len(arr)//2 :
    print(f"kth largest: {arr[len(arr)-k]}")
    print(f"kth smallest: {arr[k-1]}")
else:
    print(f"kth largest: {arr[k-1]}")
    print(f"kth smallest: {arr[len(arr)-k]}")