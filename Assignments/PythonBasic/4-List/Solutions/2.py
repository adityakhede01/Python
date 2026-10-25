# Find max and min element in array

arr = [1,5,7,8,9]
max=0
min=10 # Not a great way!

for i in range(len(arr)):
    if arr[i]>max: max=arr[i]
    if arr[i]<min: min=arr[i]

print(f"Maximum element is: {max}")
print(f"Minimum element is: {min}")