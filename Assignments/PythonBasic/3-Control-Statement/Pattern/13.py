# 1
# 01
# 101
# 0101
# 10101

for i in range(1,6):
    for j in range(1,i+1):
        # even row
        if (i%2)==0:
            if j%2==0:
                x=1
                print(x,end="")
            else:
                x=0
                print(x,end="")
        # odd row
        else:
            if j%2==0:
                x=0
                print(x,end="")
            else:
                x=1
                print(x,end="")
    print()