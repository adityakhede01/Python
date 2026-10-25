base = int(input("Enter the value of base: "))
exponent = int(input("Enter the value of exponent: "))
result = 1

for _ in range(exponent):
    result *= base

if exponent < 0:
    print("Only for positive exponent")
else:
    print(f"The result will be: {result}")