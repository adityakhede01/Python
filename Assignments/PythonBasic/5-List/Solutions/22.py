# Java program to find nearest lesser and greater element in array
# Given an array of N elements and we have to find nearest lesser and nearest greater element using C program.

a=[]
n=int(input("Enter number of elements for array: "))
for i in range(n):
    a.append(int(input(f"a[{i}]: ")))

num=int(input("Enter the number: "))

lesser=None
greater=None

for element in a:
    if element<num and (lesser is None or element>lesser):
        lesser=element
    if element>num and (greater is None or element<greater):
        greater=element

if lesser is not None: print(f"Element lesser than {num} is: {lesser}")
else: print("No lesser element found")
if greater is not None: print(f"Element greater than {num} is: {greater}")
else: print("No greater element found")