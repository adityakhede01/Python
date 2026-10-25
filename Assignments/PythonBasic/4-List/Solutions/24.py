# 24. Write a program to swap first and last element of an integer 1-d array.

arr=[1,2,3,4,5,6]

print(f"List initially: {arr}")
temp=arr[0]
arr[0]=arr[-1]
arr[-1]=temp
# Or simply => arr[0],arr[-1]=arr[-1],arr[0]
print(f"List after swapping first & last element: {arr}")