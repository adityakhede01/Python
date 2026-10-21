arr=[
    [1,2,3],
    [8,1,0],
    [3,4,5]
]

# Lower Triangle elements
for row in range(len(arr)):
    for col in range(len(arr[row])):
        if row>col:
            print(arr[row][col],end=" ")
print()
# Upper Triangle elements
for row in range(len(arr)):
    for col in range(len(arr[row])):
        if row<col:
            print(arr[row][col],end=" ")
print()
# Diagonal elements
for row in range(len(arr)):
    for col in range(len(arr[row])):
        if row==col:
            print(arr[row][col],end=" ")