# 6) WAP to find out the factors of a number.

n=int(input("Enter a number: "))
i=1
while i<=n//2:
    if n%i==0:
        print(i)
    i+=1