# 45. Find the sum of 28 terms of an Arithmetic Progression -21 -18 -15 -12 . . . . .

first_term = -21
second_term = -18
nth_term = 28
difference = second_term-first_term

sum_28_terms = (nth_term/2)*((2*first_term)+((nth_term-1)*difference))

print(f"Sum of first 28 terms: {sum_28_terms}")