# 19. Find all duplicate elements in a list and their frequencies.

l = [1, 2, 2, 3, 1, 2]
freq={}
for el in l:
    if el in freq:
        freq[el]+=1
    else:
        freq[el]=1

for el in freq:
    if freq[el]>1:
        print(el,end=" ")