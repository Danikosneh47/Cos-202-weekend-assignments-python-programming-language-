num = int(input("Enter a three-digit integer: "))

d3 = num % 10          
d2 = (num // 10) % 10  
d1 = num // 100        

if d1 < d2 < d3:
    print(f"{num} (strictly increasing)")
elif d1 > d2 > d3:
    print(f"{num} (strictly decreasing)")
elif d1 == d2 == d3:
    print(f"{num} (all equal)")
else:
    print(f"{num} (neither increasing nor decreasing)")
