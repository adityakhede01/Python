# 25. Given a nested dictionary of students and their subject marks, calculate
#     each student's total marks and find the topper.

student={
    'aditya':{
        'technical':60,
        'soft_skills':69
    },
    'alok':{
        'technical':100,
        'soft_skills':80
    }
}
for el in student:
    total=0
    for marks in student[el]:
        total += student[el][marks]
    print(f"{el} total marks are {total}")