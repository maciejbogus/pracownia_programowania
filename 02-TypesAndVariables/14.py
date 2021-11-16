#####
# Calculation of the area and circumference of a circle
##

# determine radius and PI
r = int(input("Radius: "))
PI = 3.14

# calculate area 
area = PI * (r**2)

# calculate circumference 
cir = 2 * PI * r

# display results 
print(f"Area: {area}, circumference: {cir}")
