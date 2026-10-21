# 44. Find the 28th term of an Arithmetic Progression -21 -18 -15 -12 . . . . . 

first_term = -21
second_term = -18
nth_term = 28
difference = second_term-first_term

ap_28th_term = first_term+((nth_term-1)*difference)

print(f"28th term of the given A.P.: {ap_28th_term}")