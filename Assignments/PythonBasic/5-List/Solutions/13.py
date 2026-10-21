# Find the first repeating element in array of integers

a = [10,20,30,10,40]
# found=None
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]==a[j]:
#             found = a[i]
#             break
#     if found is not None: # is not --> !=
#         print(found)
#         break
# else:
#     print("No repeating element")

# Optimized using set

result=None
s=set()
for i in range(len(a)-1,-1,-1):
    if a[i] in s:
        result=a[i]
    s.add(a[i])
print(result)