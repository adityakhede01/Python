# 12. Check whether two strings are equal without using == for the complete strings.

a="aditya is here"
b="aditya is here"

if len(a)!=len(b):
    print("Not Equal")
else:
    count=0
    for i in range(len(a)):
        if a[i]==b[i]:
            count+=1
    if count==len(a):
        print("Equal")
    else:
        print("Not Equal")