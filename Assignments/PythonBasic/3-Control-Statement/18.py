# 18) 1	2	2	4	8	32	…… n terms

first = 1
second = 2
n=int(input("Enter a number: "))
print(F"{first} {second} ",end="")
i=3
while i<=n:
    temp = first*second
    first = second
    second = temp
    print(f"{second} ",end="")
    i+=1