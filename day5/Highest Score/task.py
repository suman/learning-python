student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(max(student_scores))
max_score = 0;
for student_score in student_scores:
    if max_score < student_score:
        max_score = student_score
print(f"max sore is {max_score}")