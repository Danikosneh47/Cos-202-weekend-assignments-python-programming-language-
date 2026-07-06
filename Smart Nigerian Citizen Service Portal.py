print("==========================================")
print("   SMART NIGERIAN CITIZEN SERVICE PORTAL  ")
print("==========================================")
print("1. WAEC Result Checker\n2. JAMB Admission Adviser\n3. Voter Eligibility Checker\n4. Loan Eligibility Checker\n5. Electricity Bill Calculator\n6. Exit")
option = int(input("Select service menu option (1-6): "))

match option:
    case 1:
        maths = input("Grade in Mathematics (A1-F9): ")
        english = input("Grade in English (A1-F9): ")
        print(f"WAEC Record Verified. Core Tracks Recorded: Math [{maths}], Eng [{english}]. Status: Processed.")
    case 2:
        jamb_score = int(input("Enter JAMB Score: "))
        if jamb_score >= 200:
            print("Adviser Status: Highly Competitive for Federal Universities.")
        else:
            print("Adviser Status: Recommended to look into state colleges or polytechnics.")
    case 3:
        v_age = int(input("Enter Age: "))
        v_citizen = input("Are you a Nigerian Citizen? (Yes/No): ")
        if v_age >= 18 and v_citizen.strip().lower() == "yes":
            print("Portal Output: Eligible to register for PVC.")
        else:
            print("Portal Output: Not Eligible.")
    case 4:
        inc = float(input("Enter Monthly Salary: ₦"))
        if inc >= 100000:
            print("Loan Eligibility Status: Qualified for Standard Tier Advances.")
        else:
            print("Loan Eligibility Status: Disqualified due to risk-tier threshold.")
    case 5:
        units = float(input("Enter kilowatt-hours (kWh) consumed: "))
        
        bill = units * 120
        print(f"Calculated Post-Paid/Pre-Paid Bill Value: ₦{bill:,.2f}")
    case 6:
        print("Thank you for using the Smart Citizen Portal. Goodbye!")
    case _:
        print("Invalid Selection Code.")
