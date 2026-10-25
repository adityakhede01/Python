# 23. Write a program to find the sum and average of one dimensional integer array.

arr=[10,20,30,40,50]
sum=0
for i in range(len(arr)):
    sum+=arr[i]

average = sum/len(arr)
print(f"Sum: {sum} & average: {average}")