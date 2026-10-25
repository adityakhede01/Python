number = int(input("Enter a number: "))
reverse = 0
number_copy = number

while number_copy != 0 :
    digit = number_copy % 10
    reverse = reverse * 10 + digit
    number_copy = number_copy // 10

if number == reverse :
    print("Number is palindrome")
else:
    print("Not a palindrome number")