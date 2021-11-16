x = 1
quantity = 0
sum = 0
while 1==1:
    x=int(input("Enter number: "))
    if(x!=0):
        quantity+=1
        sum+=x
    else:
        break

print(f"RESULT: Quantity={quantity}, Sum={sum}, Mean={sum/quantity}")