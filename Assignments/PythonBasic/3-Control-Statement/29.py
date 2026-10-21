# 29) 1	11	111	1111	  11111	……

n=int(input("Enter a number: "))
for i in range(1,n+1):
    digit=1
    for j in range(1,i):
        digit=digit*10+1
    print(digit,end=" ")