a=int(input("Enter a: "))
b=int(input("Enter b: "))

for i in range(0, a):
    print("*", end="")
    for j in range(0, b-2):
        if(i==0 or i==a-1): print("*", end="")
        else: print(" ", end="")
    print("*")