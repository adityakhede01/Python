# 17) 1 	2	 4	 7	 11	 16 	…… n terms

n=int(input("Enter a number: "))
term=1
for i in range(1,n+1):
    print(term,end=" ")
    term+=i