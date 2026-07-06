print ("Defendable Digital Voting Eligibility SystemDefendable Digital Voting Eligibility System
Enter Age: 18
Are you a citizen? (Yes/No): yes
Do you have a criminal record? (Yes/No): no
Eligible to Vote

[Program finished]")
age = int(input("Enter Age: "))
citizen = input("Are you a citizen? (Yes/No): ").strip().lower()
criminal = input("Do you have a criminal record? (Yes/No): ").strip().lower()

if age >= 18 and citizen == "yes":
    if criminal == "no":
        print("Eligible to Vote")
    else:
        print("Special Verification Required (Background Check on Criminal Record)")
else:
    print("Not Eligible")
