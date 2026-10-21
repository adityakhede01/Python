# Longest consecutive sequence.
# Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.

a=[2,6,1,9,4,5,3]
# a=[1,9,3,10,4,20,2]

s = set(a)
longest=0
for num in s:
    if num-1 not in s: # Doesn't check for numbers that are already checked in consecutive sequence..
        current = num
        length=1
        while current+1 in s:
            current+=1
            length+=1
            longest = max(longest,length)
print(longest)


# -------------------------------

# # Sorted in ascending order
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# # Consecutive sequence
# sequence=1
# longest_sequence=1
# for k in range(1,len(a)):
#     if a[k]==a[k-1]+1:
#         sequence+=1
#     else:
#         # Sequence reseted !
#         sequence=1

#     if sequence>longest_sequence:
#         longest_sequence=sequence
# print(longest_sequence)