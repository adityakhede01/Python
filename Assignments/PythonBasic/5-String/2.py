# 2. Check whether a string is a palindrome.

s="abcba"
left=0
right=len(s)-1
while left<right:
    if s[left]!=s[right]:
        print("Not palindrome")
        break
    left+=1
    right-=1
else: print("Palindrome")