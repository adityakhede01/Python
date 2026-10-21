# 32) A	b	C	d	E	f	G	h	…… n terms 

n=int(input("Enter a number: "))
for i in range(n):
    if i%2==0:
        print(chr(65+i),end=" ")
    else:
        print(chr(97+i),end=" ")