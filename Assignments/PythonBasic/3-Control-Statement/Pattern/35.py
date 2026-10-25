# *****
# *  *
# * *
# **
# *

row=5
for i in range(1,row+1):
    for j in range(1,(row+1-i)+1):
        if i+j == 6 or i==1 or j==1:
            print("*",end="")
        else:
            print(" ",end="")
    print()