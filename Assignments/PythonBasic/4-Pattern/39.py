# 123456
# 54321
# 1234
# 321
# 12
# 1

n=6
for i in range(1,n+1):
    for j in range(1,n-i+1+1):
        if i%2!=0 :
            print(j,end="")
        else:
            print(n-j-i+2,end="")
    print()