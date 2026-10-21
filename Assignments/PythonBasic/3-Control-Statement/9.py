# 9) WAP to print N even numbers.

n=int(input("Enter nth number: "))
i=2
while i<=n:
    if i%2==0:
        print(i)
    i+=1