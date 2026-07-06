distance = float(input("Enter travel distance (km): "))
age = int(input("Enter passenger age: "))
is_student = input("Are you a student? (Yes/No): ").strip().lower()


if distance <= 10:
    gross_fare = 1000.0
elif distance <= 30:
    gross_fare = 1000.0 + ((distance - 10) * 80)
else:
    gross_fare = 1000.0 + (20 * 80) + ((distance - 30) * 120)

discount_pct = 0
if age > 60:
    discount_pct = 15
elif is_student == "yes":
    discount_pct = 10

if discount_pct > 20:
    discount_pct = 20

discount_val = (discount_pct / 100) * gross_fare
final_fare = gross_fare - discount_val

print("\n--- TRIP FARE SCHEDULER ---")
print(f"Distance:     {distance} km")
print(f"Gross Fare:   ₦{gross_fare:,.2f}")
print(f"Discount:     ₦{discount_val:,.2f} ({discount_pct}%)")
print(f"Final Fare:   ₦{final_fare:,.2f}")
