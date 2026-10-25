# 16. Check whether two strings are anagrams.
# Example: "listen" and "silent" → True

a="listen"
b="silent"

if len(a)!=len(b):
    print("not anagrams")
else:
    freq={}
    for ch in a:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1

    for ch in b:
        if ch not in freq or freq[ch]==0:
            print("not anagranm")
            break
        else:
            freq[ch]-=1
    else:
        print("anagram")