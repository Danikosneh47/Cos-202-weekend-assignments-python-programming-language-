num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))

if num1 < num2 and num1 < num3:
    if num2 < num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif num2 < num1 and num2 < num3:
    if num1 < num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
else:
    if num1 < num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)
Enter first integer: 4
Enter second integer: 7
Enter third integer: 9
4 7 9

[Program finished]