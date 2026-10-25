# 3. Count the number of vowels and consonants in a string.

s="aditya"
vowel="aeiouAEIOU"
vowel_c=0
consonant_c=0

for ch in s:
    if ch in vowel: vowel_c+=1
    else: consonant_c+=1
print(f"Vowel count: {vowel_c}")
print(f"consonant count: {consonant_c}")