# 29. Remove a particular character from a string without using replace().

s="aditya"
res=''
given_word='i'
replace_word='a'

for ch in s:
    if ch==given_word:
        res+=replace_word
    else:
        res+=ch
print(res)