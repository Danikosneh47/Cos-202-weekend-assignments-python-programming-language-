print ("Minimalist student result processor ")
c1 = float(input("Course 1 score: "))
c2 = float(input("Course 2 score: "))
c3 = float(input("Course 3 score: "))
c4 = float(input("Course 4 score: "))
c5 = float(input("Course 5 score: "))

total = c1 + c2 + c3 + c4 + c5
average = total / 5

if average >= 70:
    classification = "First Class"
    status = "Pass"
elif average >= 60:
    classification = "Second Class Upper"
    status = "Pass"
elif average >= 50:
    classification = "Second Class Lower"
    status = "Pass"
elif average >= 45:
    classification = "Third Class"
    status = "Pass"
else:
    classification = "Fail Profile"
    status = "Fail"

print("\n--- STUDENT SCORE PROFILE ---")
print(f"Total:          {total}")
print(f"Average:        {average:.2f}")
print(f"Classification: {classification}")
print(f"Status:         {status}")
