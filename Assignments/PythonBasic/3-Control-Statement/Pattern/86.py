# ***** *****
# ****  ****
# ***   ***
# **    **
# *     *

n=5
for i in range(1,n+1):
    for str1 in range(n-i+1,0,-1):
        print("*",end="")
    for spc in range(1,i+1):
        print(" ",end="")
    for str2 in range(n-i+1,0,-1):
        print("*",end="")
    print()