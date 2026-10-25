# 28. P is one-dimensional array of integers. Write a Java program search for a data VAL from P. If VAL is present in the array then “element found ” otherwise “element not found” should be displayed. 

P=[10,20,30,40,50,60,70]
VAL=int(input("Enter a number to search: "))
for i in range(len(P)):
    if P[i]==VAL:
        print("Element found")
        break
else: print("Element not found")