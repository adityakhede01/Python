# Sub with equal 0s and 1s
# Given an array containing 0s and 1s. Find the number of subarrays having equal number of 0s and 1s.

a=[1,0,0,1,0,1,1,0,1,0,1,1,0]
for i in range(len(a)):
    zc=0
    oc=0
    for j in range(i,len(a)):
        if a[j]==0:
            zc+=1
        if a[j]==1:
            oc+=1
        if zc==oc:
            print(f"({i},{j})",end=" ")