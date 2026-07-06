print ( "Exam metrics evaluator")
s1 = float(input("Enter score 1: "))
s2 = float(input("Enter score 2: "))
s3 = float(input("Enter score 3: "))

average = (s1 + s2 + s3) / 3

if average >= 80:
    print(f"Average: {average:.2f} -> Excellent Student")
elif 60 <= average < 80:
    print(f"Average: {average:.2f} -> Good Student")
elif 50 <= average < 60:
    print(f"Average: {average:.2f} -> Average Student")
else:
    print(f"Average: {average:.2f} -> Probation Student")
