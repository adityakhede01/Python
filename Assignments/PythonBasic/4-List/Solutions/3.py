# Two Pointer approach
# Reverse the array

arr = [1,5,7,8,9]
first = 0
end = len(arr)-1

print(f"Before updation: {arr}")

while first<=end:
    arr[first],arr[end] = arr[end],arr[first]
    first+=1
    end-=1

print(f"After updation: {arr}")