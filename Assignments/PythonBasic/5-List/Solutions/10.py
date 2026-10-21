# Write a program to cyclically rotate array by one.

a = [10,20,30,40,50]
item=a[len(a)-1] # Well -1 also does the same thing.
for i in range(len(a)-1,0,-1):
    a[i]=a[i-1]
a[0]=item
print(a)

# To rotaate by k run the loop k times.