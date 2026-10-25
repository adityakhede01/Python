n = int(input("Enter a number to check whether it is armstrong or not: "))
length = 0
temp = n
sum = 0

while n!=0 :
    length += 1
    n = n//10

n = temp

while n!=0 :
    value = n % 10
    sum = sum + (value**length)
    n = n//10

if sum == temp :
    print(f"Number is Armstrong.")
else :
    print(f"Not Armstrong.")