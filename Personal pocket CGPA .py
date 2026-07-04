print("=== PERSONAL POCKET CGPA CALCULATOR (PPC) ===")

def grade_to_point(grade):
    if grade.upper() == "A":
        return 5
    elif grade.upper() == "B":
        return 4
    elif grade.upper() == "C":
        return 3
    elif grade.upper() == "D":
        return 2
    elif grade.upper() == "E":
        return 1
    elif grade.upper() == "F":
        return 0
    else:
        print("Invalid grade entered! Please use A-F.")
        return None


num_courses = int(input("Enter number of courses taken: "))

total_points = 0
total_units = 0

for i in range(num_courses):
    print(f"\nCourse {i+1}:")
    grade = input("Enter grade (A-F): ")
    units = int(input("Enter credit units: "))
    
    point = grade_to_point(grade)
    if point is not None:
        total_points += point * units
        total_units += units


if total_units > 0:
    cgpa = total_points / total_units
    print("\n=== RESULT ===")
    print(f"Total Credit Units: {total_units}")
    print(f"Total Grade Points: {total_points}")
    print(f"Your CGPA is: {cgpa:.2f}")
    
   
    if cgpa >= 4.5:
        print("Classification: First Class")
    elif cgpa >= 3.5:
        print("Classification: Second Class Upper")
    elif cgpa >= 2.5:
        print("Classification: Second Class Lower")
    elif cgpa >= 1.5:
        print("Classification: Third Class")
    else:
        print("Classification: Pass")
else:
    print("No valid courses entered. CGPA cannot be calculated.")