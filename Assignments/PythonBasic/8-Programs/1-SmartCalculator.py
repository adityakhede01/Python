'''
1. Smart Calculator
Beginner
Concepts: if-elif-else, while, functions
Requirements
* Display a menu for addition, subtraction, multiplication, division, and modulus.
* Take two numbers from the user.
* Use separate functions for each operation.
* Handle division by zero.
* Repeat until the user selects Exit.
Bonus: Add power and floor division operations.
'''

def input_num():
    first=float(input("Enter first number: "))
    second=float(input("Enter second number: "))
    return first,second

def menu():
    while(1):
        print("+ -> 1 || - -> 2 || * -> 3 || / -> 4 || % -> 5 || ** -> 6 || // -> 7 || exit -> e")
        ch = input("Select an option: ")
        match ch:
            case '1':
                res = input_num()
                print(res[0]+res[1])
            case '2':
                res = input_num()
                print(res[0]-res[1])
            case '3':
                res = input_num()
                print(res[0]*res[1])
            case '4':
                res = input_num()
                if res[1]==0:
                    print("Division cann't be peformed by 0")
                    break
                print(res[0]/res[1])
            case '5':
                res = input_num()
                print(res[0]%res[1])
            case '6':
                res = input_num()
                print(res[0]**res[1])
            case '7':
                res = input_num()
                print(res[0]/res[1])
            case 'e':
                break
            case _:
                print("Invalid option")
menu()