# 55555
# 4  4
# 3 3
# 22
# 1

row=5
for i in range(1,row+1):
    for j in range(1,(row+1-i)+1):
        if i==1 or j==1 or i+j==6:
            print(row-i+1,end="")
        else:
            print(" ",end="")
    print()