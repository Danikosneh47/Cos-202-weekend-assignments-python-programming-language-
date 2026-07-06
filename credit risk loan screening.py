print (" Credit risk loan screening")
age = int(input("Enter Age: "))
income = float(input("Enter Monthly Income (₦): "))
experience = int(input("Enter Years of Employment: "))
has_loan = input("Have an existing loan? (Yes/No): ").strip().lower()
rating = input("Enter Credit Rating (Excellent, Good, Fair, Poor): ").strip().lower()


rejected = False
conditions = False


if age < 18 or income < 50000 or experience < 1 or rating == "poor":
    rejected = True

if has_loan == "yes" or rating == "fair":
    conditions = True

if rejected:
    print("\n--- Application Result: Loan Rejected ---")
    if age < 18: print("- Applicant is underage (Must be 18+).")
    if income < 50000: print("- Monthly income below stable threshold.")
    if experience < 1: print("- Employment stability insufficient (< 1 year experience).")
    if rating == "poor": print("- Risk index too high: Poor Credit Rating.")
elif conditions:
    print("\n--- Application Result: Loan Approved with Conditions ---")
    if has_loan == "yes": print("- Subject to consolidation of existing loan profile.")
    if rating == "fair": print("- Subject to higher variable interest margins due to Fair Rating.")
else:
    print("\n--- Application Result: Loan Approved ---")
