import random

names = ["sanjay", "praba", "ila", "magesh"]

student_dict = {student: random.randint(1, 100) for student in names}
print(student_dict)
passed_students = {student: score for (student, score) in student_dict.items() if score >= 60}
print(passed_students)