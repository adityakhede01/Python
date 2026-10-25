# 5. Count the number of words in a sentence.

s="aditya is solving some string problems."

# print(s.split()) => ['aditya', 'is', 'solving', 'some', 'string', 'problems.']
# print(len(s.split()))

count=0
in_word=False
for ch in s:
    if ch !=' ' and not in_word:
        count+=1
        in_word=True
    elif ch==' ':
        in_word=False
print("Word count: ",count)