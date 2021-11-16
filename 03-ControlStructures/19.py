x=int(input("Enter dog's age: "))
age=0

for i in range(1, x+1):
    if(i<=2):
        age+=10.5
    else:
        age+=4

print(f"The dog's age in dog’s years is {int(age)} years")