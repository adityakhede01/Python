'''
2. Student Result Management System
Beginner
Concepts: Conditions, loops, functions
Requirements
* Input marks for five subjects.
* Calculate total, percentage, and grade.
* Check whether the student passed or failed.
* Validate that each mark is between 0 and 100.
* Create functions such as calculate_total(), calculate_percentage(), and calculate_grade().
Bonus: Accept results for multiple students and calculate the class average.
'''

first=float(input("Enter marks of subject 1: "))
second=float(input("Enter marks of subject 2: "))
third=float(input("Enter marks of subject 3: "))
fourth=float(input("Enter marks of subject 4: "))
fifth=float(input("Enter marks of subject 5: "))

total = first+second+third+fourth+fifth
percentage = total/5

def calculate_total():
    print(f'Total is: {total}')
def calculate_percentage():
    print(f'Percentage is: {percentage}')
def calculate_grade():
    if percentage>=60:
        print("Student Pass")
    else:
        print("Student failed")

if (0<=first<=100) or (0<=second<=100) or (0<=third<=100) or (0<=fourth100) or (0<=fifth<=100):
    calculate_total()
    calculate_percentage()
    calculate_grade()
else:
    print("Marks aren't in between 0 and 100")