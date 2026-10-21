# 11) WAP to print N odd numbers.

n=int(input("Enter nth number: "))
i=1
while i<=n:
    if i%2!=0:
        print(i)
    i+=1