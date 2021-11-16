import math

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

if(a+b>c and c+b>a and a+c>b):
    s=(a+b+c)/2
    area = math.sqrt(a*(s-a)*(s-b)*(s-c))

    print(f"Area: {area}")
    
else:
    print("This is not triangle")