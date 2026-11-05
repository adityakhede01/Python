# 32. Find the longest palindromic substring.
# Example: "babad" → "bab" or "aba"

s = "babad"
res=''
max=float('-inf')
for i in range(len(s)):
    a=''
    for j in range(i,len(s)):
        a+=s[j]
        if a == a[::-1]:
            if len(a)>max:
                max=len(a)
                res=a
print(res)

'''
def longestPalindrome(s):
    res = ""

    for i in range(len(s)):

        # Odd length palindrome
        l = r = i

        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(res):
                res = s[l:r+1]

            l -= 1
            r += 1

        # Even length palindrome
        l, r = i, i + 1

        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(res):
                res = s[l:r+1]

            l -= 1
            r += 1

    return res


print(longestPalindrome("babad"))
'''