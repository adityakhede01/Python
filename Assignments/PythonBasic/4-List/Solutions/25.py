# 25. Write a program to reverse the element of an integer 1-D array. 

# l=[1,2,3,4,5]
l=[1,2,3,4,5,6]

print(f"List initially: {l}")
for i in range(len(l)//2):
    l[i],l[len(l)-i-1]=l[len(l)-i-1],l[i]
print(f"List after reversing all elements: {l}")