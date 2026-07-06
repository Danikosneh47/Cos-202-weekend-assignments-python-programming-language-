jamb = int(input("Enter JAMB Score: "))
credits = int(input("Enter Number of O'Level Credits: "))
age = int(input("Enter Age: "))

if jamb >= 300 and credits >= 8 and age >= 16:
    print("Scholarship Candidate")
elif jamb >= 200 and credits >= 5 and age >= 16:
    print("Admission Offered")
else:
    print("Admission Denied")
    print("Reason(s) for Denial:")
    if jamb < 200:
        print(f"- Low JAMB Score ({jamb}/200 minimum required)")
    if credits < 5:
        print(f"- Insufficient O'Level Credits ({credits}/5 minimum required)")
    if age < 16:
        print(f"- Underage ({age}/16 years minimum required)")
