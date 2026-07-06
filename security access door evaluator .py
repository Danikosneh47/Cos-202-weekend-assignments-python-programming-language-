print ( "security door  access evaluator")
pw = input("Password correct? (Yes/No): ").strip().lower()
fp = input("Fingerprint verified? (Yes/No): ").strip().lower()
face = input("Face recognition successful? (Yes/No): ").strip().lower()

count = 0
if pw == "yes": count += 1
if fp == "yes": count += 1
if face == "yes": count += 1

if count >= 2:
    print("Access Granted: The door opens.")
else:
    print("Access Denied: Insufficient credentials verified.")
