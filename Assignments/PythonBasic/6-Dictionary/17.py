# 17. Count the frequency of each number in a list.
# Example: [1, 2, 2, 3, 1, 2] -> {1: 2, 2: 3, 3: 1}

l = [1, 2, 2, 3, 1, 2]
freq={}
for el in l:
    if el in freq:
        freq[el]+=1
    else:
        freq[el]=1
print(freq)