# 28. Check whether one string is a rotation of another.
# Example: "abcd" and "cdab" → True

first="abcd"
second="cdab"

if second in first*2:
    print(True)
else:
    print(False)