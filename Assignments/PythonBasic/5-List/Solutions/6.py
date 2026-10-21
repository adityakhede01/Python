# Sort the arrays of 0s, 1s and 2s

arr = [0,1,1,2,0,2,0,1]
zc=0
oc=0
tc=0

for element in arr:
    if element==0:
        zc+=1
    elif element==1:
        oc+=1
    else:
        tc+=1

for i in range(zc):
    arr[i]=0
for i in range(zc,zc+oc):
    arr[i]=1
for i in range(zc+oc,zc+oc+tc):
    arr[i]=2

print(arr)