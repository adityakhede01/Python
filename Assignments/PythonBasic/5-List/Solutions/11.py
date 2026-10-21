# Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.

# a = [1, 1, 1, 1] and K=2
a = [1,5,7,1]
K = 6; count =0

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==K:
            count+=1
print(count)