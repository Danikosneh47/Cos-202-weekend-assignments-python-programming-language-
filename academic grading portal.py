print ( "Academic grading portal")
ca = float(input("Enter CA Score (Max 30): "))
exam = float(input("Enter Exam Score (Max 70): "))
attendance = float(input("Enter Attendance (%): "))

total_score = ca + exam

if attendance < 75:
    grade = 'F'
else:
    if 70 <= total_score <= 100:
        grade = 'A'
    elif 60 <= total_score <= 69:
        grade = 'B'
    elif 50 <= total_score <= 59:
        grade = 'C'
    elif 45 <= total_score <= 49:
        grade = 'D'
    else:
        grade = 'F'

print("\n--- RESULTS ---")
print(f"Total Score: {total_score}")
print(f"Grade:       {grade}")
