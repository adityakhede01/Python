# 4. Count uppercase letters, lowercase letters, digits, and special characters.

# Whitespace: Space,\t,\n => isspace()

s="Aditya@123# PRO"
u_c=0
l_c=0
d_c=0
s_c=0
for ch in s:
    if 'A'<=ch<='Z':
        u_c+=1
    elif 'a'<=ch<='z':
        l_c+=1
    elif '0'<=ch<='9':
        d_c+=1
    elif ch==' ':
        continue # whitespace character
    else:
        s_c+=1

print(f"Uppercase letter count: {u_c}")
print(f"Lowercase letter count: {l_c}")
print(f"Digits letter count: {d_c}")
print(f"Special letter count: {s_c}")