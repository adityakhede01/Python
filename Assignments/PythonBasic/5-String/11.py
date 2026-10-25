# 11. Count how many times a particular character occurs.

s="aditya is here"
val="i"
count=0
for ch in s:
    if val==ch: count+=1
print(count)