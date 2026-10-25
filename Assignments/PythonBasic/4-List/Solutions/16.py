# Rearrange the array in alternating positive and negative items
# Given an unsorted array Arr of N positive and negative numbers. Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.
# Note: Array should start with positive number.

# a=[9, 4, -2, -1, 5, 0, -5, -3, 2]
a=[-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
pos=[]
neg=[]
res=[]
i=0
j=0

for element in a:
    if element<0:
        neg.append(element)
    else:
        pos.append(element)

while i<len(pos) and j<len(neg):
    res.append(pos[i])
    res.append(neg[i])
    i+=1
    j+=1
while i<len(pos):
    res.append(pos[i])
    i+=1

print(res)