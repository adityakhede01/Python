# 31) 9	99	999	9999	  99999 …….

n=int(input("Enter a number: "))
for i in range(1,n+1):
    digit=9
    for j in range(1,i):
        digit=digit*10+9
    print(digit,end=" ")