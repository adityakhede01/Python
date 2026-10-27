# 31. Find the longest substring without repeating characters.
# Example: "abcabcbb" → 3 ("abc")

s='abcabcbb'
left=0
right=0
res=''
longest_sub=''

while right < len(s):
    if s[right] in res:
        while s[right] in res:
            res = res[1:] # Remove first character of res string
            left+=1
    else:
        res+=s[right]
        right+=1
        if len(res) > len(longest_sub):
            longest_sub = res

print(f'{len(longest_sub)} ("{longest_sub}")')

# Note: Optimize with dictionary later