print("1 - Regular\n2 - Silver\n3 - Gold")
category = int(input("Enter Customer Category (1-3): "))
purchase = float(input("Enter Purchase Amount (₦): "))
day = input("Is today Friday? (Yes/No): ").strip().lower()

discount_pct = 0
category_name = ""

if category == 1:
    category_name = "Regular"
    if purchase > 20000:
        discount_pct = 5
elif category == 2:
    category_name = "Silver"
    if 20001 <= purchase <= 50000:
        discount_pct = 10
    elif purchase > 50000:
        discount_pct = 15
elif category == 3:
    category_name = "Gold"
    discount_pct = 20
else:
    category_name = "Unknown"


if day == "yes":
    discount_pct += 5


if discount_pct > 25:
    discount_pct = 25

discount_value = (discount_pct / 100) * purchase
final_payable = purchase - discount_value

print("\n--- TRANSACTION RECEIPT ---")
print(f"Customer Category:  {category_name}")
print(f"Purchase Amount:    ₦{purchase:,.2f}")
print(f"Total Discount (%): {discount_pct}%")
print(f"Discount Value:     ₦{discount_value:,.2f}")
print(f"Final Amount Due:   ₦{final_payable:,.2f}")
