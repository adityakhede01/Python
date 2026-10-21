# 5) WAP to find out the factorial of a number.

n=int(input("Enter a number: "))
fact=1
while n>=1:
    fact*=n
    n-=1

print(f"Factorial of n is: {fact}")