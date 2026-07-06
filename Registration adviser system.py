print ( "Registration adviser system")
level = int(input("Enter Level (100-500): "))
cgpa = float(input("Enter CGPA: "))
fees_outstanding = input("Outstanding Fees? (Yes/No): ").strip().lower()
reg_status = input("Is course registration active? (Yes/No): ").strip().lower()

match reg_status:
    case "no":
        print("Advice: Registration Closed")
    case "yes":
        if fees_outstanding == "yes":
            print("Advice: Clear Outstanding Fees")
        elif cgpa < 1.50:
            print("Advice: Academic Probation - Meet Your Adviser")
        elif level >= 400 and cgpa >= 1.50:
            print("Advice: Registration Approved & Graduation Eligible")
        else:
            print("Advice: Registration Approved")
