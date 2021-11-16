x=int(input("Enter x: "))
y=int(input("Enter y: "))

if(x > 0):
    if(y > 0):
        quadrant = "first quadrant"
    else:
        quadrant = "fourth quadrant"
elif(x < 0):
    if(y > 0):
        quadrant = "second quadrant"
    elif(y < 0):
        quadrant = "third quadrant"
else:
    quadrant = "middle"

print(f"Point P({x}, {y}) is in the {quadrant} of the coordinate system")