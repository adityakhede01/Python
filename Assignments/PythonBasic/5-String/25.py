# 25. Check whether a string contains only digits without using isdigit().

s="12345678"
digits="0123456789"
for ch in s:
    if ch not in digits:
        print("Invalid string")
        break
else:
    print("String contains only digits")