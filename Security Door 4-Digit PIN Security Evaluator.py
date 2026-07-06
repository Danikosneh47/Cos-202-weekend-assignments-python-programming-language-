print ( "Security Door 4-Digit PIN Security Evaluator")
pin = int(input("Enter a 4-digit security PIN: "))

d4 = pin % 10
d3 = (pin // 10) % 10
d2 = (pin // 100) % 10
d1 = pin // 1000

middle_pair = (d2 * 10) + d3
digit_sum = d1 + d2 + d3 + d4
edge_product = d1 * d4

if pin < 1000 or pin > 9999:
    print("Access Denied: PIN must have exactly 4 digits.")
elif (d1 + d4) % 2 != 0:
    print("Access Denied: Sum of first and last digit is not even.")
elif (middle_pair % 7 != 0) and (middle_pair % 13 != 0):
    print("Access Denied: Middle pair not a multiple of 7 or 13.")
elif digit_sum <= edge_product:
    print("Access Denied: Sum of all digits must be greater than product of edge digits.")
else:
    print("Access Granted")
