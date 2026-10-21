# 8) WAP to print Fibonacci series.
# 1,1,2,3,5,8,...

first = 1
second = 1
n=int(input("Enter number till you want fibonacci series: "))
print(F"{first} {second} ",end="")
i=3
while i<=n:
    temp = first+second
    first = second
    second = temp
    print(f"{second} ",end="")
    i+=1